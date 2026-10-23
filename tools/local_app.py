"""Offline desktop launcher: a browser UI served only on 127.0.0.1."""
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import argparse
import json
import mimetypes
import os
import secrets
import subprocess
import sys
import threading
import urllib.parse
import webbrowser

ROOT=Path(__file__).resolve().parents[1]
PRIVATE=ROOT/'private/local-review'
TOKEN=secrets.token_urlsafe(32)
LOCK=threading.Lock()
JOB={'running':False,'lines':[],'report':None,'exit_code':None}

def settings():
    dev=ROOT.parent/'beyblade-translation'
    result={'rom':str(next(ROOT.parent.glob('*Saikyou*.gba'),'')),
        'core':str(dev/'emulator/mgba_libretro.dll'),
        'story_state':str(dev/'battle-open.state'),'battle_state':str(dev/'launch-power.state'),
        'kind':'battle','scope':'all','count':3,'resources':''}
    try:result.update(json.loads((PRIVATE/'settings.json').read_text('utf-8')))
    except (OSError,ValueError):pass
    return result

def start_job(config):
    with LOCK:
        if JOB['running']:raise ValueError('Já existe uma execução em andamento.')
        assert config['kind'] in ('battle','story') and config['scope'] in ('all','changed')
        count=int(config['count']);assert 1<=count<=20
        for key in ('rom','core',config['kind']+'_state'):
            if not Path(config[key]).is_file():raise ValueError('Arquivo não encontrado: '+str(config[key]))
        PRIVATE.mkdir(parents=True,exist_ok=True)
        (PRIVATE/'settings.json').write_text(json.dumps(config,indent=2),encoding='utf-8')
        cancel=PRIVATE/'cancel.request';cancel.unlink(missing_ok=True)
        JOB.update(running=True,lines=[],report=None,exit_code=None)
    command=[sys.executable,str(ROOT/'tools/qa_runner.py'),'--rom',config['rom'],
        '--core',config['core'],'--state',config[config['kind']+'_state'],
        '--kind',config['kind'],'--scope',config['scope'],'--count',str(count),'--cancel-file',str(cancel),
        '--resources',str(config.get('resources',''))]
    def worker():
        try:
            process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,
                encoding='utf-8',errors='replace',env={**os.environ,'PYTHONIOENCODING':'utf-8'},
                creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            for line in process.stdout:
                line=line.rstrip()
                with LOCK:
                    JOB['lines'].append(line)
                    if line.startswith('REPORT='):JOB['report']=str(Path(line[7:]).resolve())
            code=process.wait()
        except Exception as error:
            with LOCK:JOB['lines'].append('ERRO: '+str(error))
            code=1
        with LOCK:JOB.update(running=False,exit_code=code)
    threading.Thread(target=worker,daemon=True).start()

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def send(self,data,status=200,kind='application/json'):
        if not isinstance(data,bytes):data=(json.dumps(data,ensure_ascii=False) if kind=='application/json' else data).encode('utf-8')
        self.send_response(status);self.send_header('Content-Type',kind+'; charset=utf-8')
        self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(data)
    def authorized(self):
        host=self.headers.get('Host','')
        params=urllib.parse.parse_qs(urllib.parse.urlsplit(self.path).query)
        supplied=self.headers.get('X-Local-Token') or params.get('token',[''])[0]
        return host==f'127.0.0.1:{self.server.server_port}' and secrets.compare_digest(supplied,TOKEN)
    def do_GET(self):
        if not self.authorized():self.send({'error':'Acesso local inválido.'},403);return
        path=urllib.parse.urlsplit(self.path).path
        if path=='/':self.send((ROOT/'tools/local_app.html').read_text('utf-8'),kind='text/html')
        elif path=='/settings':self.send(settings())
        elif path=='/status':
            with LOCK:self.send(dict(JOB))
        elif path.startswith('/report/'):
            with LOCK:report=JOB['report']
            if not report:self.send({'error':'Sem relatório.'},404);return
            folder=Path(report).parent.resolve();file=(folder/urllib.parse.unquote(path[8:])).resolve()
            if not file.is_relative_to(folder) or not file.is_file() or file.suffix not in ('.html','.png','.json'):
                self.send({'error':'Arquivo indisponível.'},404);return
            data=file.read_bytes()
            if file.suffix=='.html':
                # Keep the report's relative image links authenticated on this local server.
                import re
                text=data.decode('utf-8')
                text=re.sub(r'(href|src)="([^":]+\.png)"',lambda m:f'{m[1]}="{m[2]}?token={TOKEN}"',text)
                data=text.encode('utf-8')
            self.send(data,kind=mimetypes.guess_type(file.name)[0] or 'application/octet-stream')
        else:self.send({'error':'Não encontrado.'},404)
    def do_POST(self):
        if not self.authorized():self.send({'error':'Acesso local inválido.'},403);return
        origin=self.headers.get('Origin')
        if origin and origin!=f'http://127.0.0.1:{self.server.server_port}':self.send({'error':'Origem inválida.'},403);return
        try:
            length=int(self.headers.get('Content-Length','0'));assert 0<=length<=32768
            body=json.loads(self.rfile.read(length) or b'{}')
            path=urllib.parse.urlsplit(self.path).path
            if path=='/run':start_job(body);self.send({'ok':True})
            elif path=='/cancel':
                PRIVATE.mkdir(parents=True,exist_ok=True);(PRIVATE/'cancel.request').touch();self.send({'ok':True})
            elif path=='/shutdown':
                with LOCK:running=JOB['running']
                if running:raise ValueError('Cancele e aguarde o teste atual antes de encerrar.')
                self.send({'ok':True});threading.Thread(target=self.server.shutdown,daemon=True).start()
            else:self.send({'error':'Não encontrado.'},404)
        except (ValueError,AssertionError,KeyError,TypeError,OSError) as error:self.send({'error':str(error) or 'Configuração inválida.'},400)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--no-browser',action='store_true');args=parser.parse_args()
    active=PRIVATE/'active-app.json'
    try:
        import urllib.request
        previous=json.loads(active.read_text('utf-8'))['url']
        parsed=urllib.parse.urlsplit(previous)
        assert parsed.scheme=='http' and parsed.hostname=='127.0.0.1'
        check=urllib.parse.urlunsplit((parsed.scheme,parsed.netloc,'/status',parsed.query,''))
        with urllib.request.urlopen(check,timeout=1) as response:assert response.status==200
        if not args.no_browser:webbrowser.open(previous)
        print('Aplicativo já está em execução: '+previous,flush=True);return
    except (OSError,ValueError,KeyError,AssertionError):pass
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    url=f'http://127.0.0.1:{server.server_port}/?token={TOKEN}'
    PRIVATE.mkdir(parents=True,exist_ok=True)
    active.write_text(json.dumps({'url':url}),encoding='utf-8')
    print('Aplicativo local: '+url,flush=True)
    if not args.no_browser:webbrowser.open(url)
    try:server.serve_forever(poll_interval=0.3)
    except KeyboardInterrupt:pass
    finally:
        server.server_close()
        active.unlink(missing_ok=True)

if __name__=='__main__':main()
