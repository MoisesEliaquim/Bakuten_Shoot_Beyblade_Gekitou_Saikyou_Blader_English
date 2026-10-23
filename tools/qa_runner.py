"""Offline build, deterministic sample selection, emulator fixtures, and review report."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import html
import json
import os
import struct
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE_HASH='58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c'

def read_json(path): return json.loads(path.read_text('utf-8'))
def digest(data): return hashlib.sha256(data).hexdigest()

def run_command(command,log):
    with log.open('w',encoding='utf-8') as output:
        result=subprocess.run(command,stdout=output,stderr=subprocess.STDOUT,
                              env={**os.environ,'PYTHONIOENCODING':'utf-8'},
                              creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    if result.returncode:
        raise RuntimeError(f'{Path(command[1]).name} falhou. '+log.read_text('utf-8',errors='replace')[-1800:])

def select_resources(kind,limit,scope,profile,resource_filter=''):
    if kind=='story':
        sources=read_json(ROOT/'translations/dialogue-en.json')
        manifest=read_json(ROOT/'build/narrow-manifest.json')['scenes']
        records=[dict(e,id=e['scene'],source=sources[str(e['scene'])]) for e in manifest]
    else:
        sources={e['resource']:e for e in read_json(ROOT/'translations/battle-en.json')}
        records=[dict(e,id=e['resource'],source=sources[e['resource']]) for e in read_json(ROOT/'build/battle-manifest.json')]
    if resource_filter:
        wanted=set()
        for fragment in resource_filter.split(','):
            bounds=fragment.strip().split('-')
            assert len(bounds) in (1,2) and all(x.isdigit() for x in bounds),'Filtro de recursos inválido.'
            first=int(bounds[0]);last=int(bounds[-1])
            assert 0<=first<=last<=2000,'Intervalo de recursos inválido.'
            wanted.update(range(first,last+1))
        available={e['id'] for e in records}
        assert wanted<=available,'O filtro inclui recursos ainda não traduzidos: '+str(sorted(wanted-available))
        records=[e for e in records if e['id'] in wanted]
    cache=ROOT/'private/local-review'/f'{kind}-last-tested.json'
    previous=read_json(cache) if cache.exists() else {}
    for e in records:
        e['source_hash']=digest(json.dumps(e['source'],sort_keys=True,ensure_ascii=False).encode()+profile.encode())
    changed=[e for e in records if previous.get(str(e['id']))!=e['source_hash']]
    candidates=changed if scope=='changed' else records
    selected=sorted(candidates,key=lambda e:(-e['bytes'],e['id']))[:limit]
    # Keep new control formats and dynamic-name cases in addition to the sample.
    extra=[]
    if scope=='changed':
        for e in changed:
            text=json.dumps(e['source'],ensure_ascii=False)
            if ('{N1}' in text or '{N2}' in text or '"speaker": null' in text) and e not in selected:
                extra.append(e)
    return selected+extra,cache,len(candidates)

def write_report(run,report):
    (run/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    cards=[]
    for item in report['resources']:
        shots=''.join(f'<a href="{html.escape(p)}" target="_blank"><img loading="lazy" src="{html.escape(p)}"></a>' for p in item['screenshots'])
        cards.append(f'<section><h2>Recurso {item["id"]} · {item["bytes"]} bytes</h2><p>{html.escape(item["status"])}</p>'
                     f'<label>Revisão visual: <select data-id="{item["id"]}"><option>Pendente</option><option>Aprovado</option><option>Revisar</option></select></label>'
                     f'<pre>{html.escape(item["translation"])}</pre><div class="shots">{shots}</div></section>')
    page='''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Revisão local Beyblade</title>
<style>body{font:16px system-ui;background:#101923;color:#e6edf5;margin:30px;max-width:1400px}section{background:#1b2b3d;padding:20px;margin:20px 0;border-radius:12px}img{width:240px;height:160px;image-rendering:pixelated;border:1px solid #52657b}.shots{display:flex;flex-wrap:wrap;gap:8px}pre{white-space:pre-wrap}select,button{padding:8px}a{color:#8ed2ff}</style>
<h1>Revisão local da tradução</h1>'''
    page+=f'<p>Resultado: <strong>{html.escape(report["status"])}</strong> · {html.escape(report["version"])}</p>'
    page+='<p>A execução e as imagens são locais. Nenhuma imagem foi enviada a uma IA. As verificações automáticas não comprovam fidelidade da tradução, ausência de cortes, campanha completa ou acionamento natural das cenas.</p>'
    page+='<p>As marcações abaixo são pessoais e ficam no armazenamento deste navegador. Não alteram a ROM nem equivalem à aprovação automática.</p><button onclick="exportReview()">Exportar minha revisão</button>'
    if report.get('error'):page+='<pre>'+html.escape(report['error'])+'</pre>'
    page+=''.join(cards)
    page+='<script>const reviewRun='+json.dumps(run.name)+';</script>'
    page+='''<script>
const key='beyblade-review:'+reviewRun;let marks={};try{marks=JSON.parse(localStorage.getItem(key)||'{}')}catch{}
document.querySelectorAll('select').forEach(el=>{el.value=marks[el.dataset.id]||'Pendente';el.onchange=()=>{marks[el.dataset.id]=el.value;try{localStorage.setItem(key,JSON.stringify(marks))}catch{}}});
function exportReview(){const b=new Blob([JSON.stringify({report:location.pathname,review:marks},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='revisao-visual.json';a.click();URL.revokeObjectURL(a.href)}
</script></html>'''
    (run/'report.html').write_text(page,encoding='utf-8')

def execute(args):
    rom=args.rom.resolve();core=args.core.resolve();state=args.state.resolve()
    assert rom.is_file() and digest(rom.read_bytes())==SOURCE_HASH,'Selecione a ROM japonesa original AHEJ compatível.'
    assert core.is_file(),'Núcleo mGBA não encontrado.'
    assert state.is_file(),'Estado salvo de teste não encontrado.'
    assert 900<=args.battle_frames<=20000,'Janela de batalha inválida.'
    assert 1<=args.count<=20,'A amostra deve ter entre 1 e 20 cenas.'
    run=ROOT/'build/qa'/dt.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    run.mkdir(parents=True)
    project=read_json(ROOT/'project.json')
    report={'status':'executando','version':project['version'],'kind':args.kind,'resources':[],
            'source_sha256':SOURCE_HASH,'visual_review':'pending','natural_triggers_verified':False}
    print(f'RUN_DIR={run}',flush=True)
    try:
        print('Reconstruindo e verificando o IPS...',flush=True)
        run_command([sys.executable,str(ROOT/'tools/build.py'),'--rom',str(rom)],run/'build.log')
        output=ROOT/'build'/(project['artifact_stem']+'.gba')
        data=output.read_bytes();report['patched_sha256']=digest(data)
        report['automatic_build_and_ips']='passed'
        engine=b''.join((ROOT/'tools'/name).read_bytes() for name in ['build_dialogue.py','build_ui.py','battle_patch.py','qa_emulator.py','qa_runner.py'])
        profile=digest(engine+core.read_bytes()+state.read_bytes()+str(args.battle_frames).encode())
        selected,cache,candidates=select_resources(args.kind,args.count,args.scope,profile,args.resources)
        report['resource_filter']=args.resources
        report['candidate_count']=candidates
        report['selection']='Largest encoded resources; changed scope also includes changed dynamic names and headerless formats.'
        previous=read_json(cache) if cache.exists() else {}
        for number,e in enumerate(selected,1):
            if args.cancel_file and args.cancel_file.exists():
                report['status']='cancelado';break
            print(f'Teste {number}/{len(selected)}: recurso {e["id"]}',flush=True)
            folder=run/f'{args.kind}-{e["id"]}';folder.mkdir()
            offset=int(e['new_offset'],16);fixture=bytearray(data)
            common=[sys.executable,str(ROOT/'tools/qa_emulator.py'),'--core',str(core),
                    '--output-dir',str(folder),'--load-state',str(state),'--output','final.png']
            context_scene=None
            if args.kind=='story':
                if e['source'][0]['speaker'] is None:
                    dialogue=read_json(ROOT/'translations/dialogue-en.json')
                    eligible=[int(scene) for scene,messages in dialogue.items()
                              if int(scene)<e['id'] and messages and messages[-1]['speaker'] is not None]
                    context_scene=max(eligible,default=604)
                    context=next(x for x in read_json(ROOT/'build/narrow-manifest.json')['scenes'] if x['scene']==context_scene)
                    p=int(context['new_offset'],16)
                    context_data=data[p:p+context['bytes']]
                    trim=4 if context_data.endswith(b'WWEE') else 2 if context_data.endswith(b'EE') else 0
                    assert trim,'Unsupported headerless-scene test context ending.'
                    payload=context_data[:-trim]+b'PP'+data[offset:offset+e['bytes']]
                    offset=0x4F0000
                    assert all(v==255 for v in fixture[offset:offset+len(payload)])
                    fixture[offset:offset+len(payload)]=payload
                struct.pack_into('<I',fixture,0x31CD4C+353*4,offset-0x31CD4C)
                frames=max(1200,(data[int(e['new_offset'],16):int(e['new_offset'],16)+e['bytes']].count(b'PP')+4)*240)
                assert frames<=20000,'Cena excede o limite do perfil de teste.'
                extra=['--frames',str(frames),'--buttons','A','--pulse','600','--pulse-width','1','--capture-every','54','--initial-buttons','B','--initial-frames','3']
                translation='\n\n'.join(m['text'] for m in e['source'])
            else:
                extra=['--frames',str(args.battle_frames),'--buttons','A','--capture-every','54','--capture-from','330',
                       '--test-battle-resource',str(e['id']),'--test-battle-frame','310']
                translation='\n\n'.join(e['source']['english_pages'])
            testrom=folder/'fixture.gba';testrom.write_bytes(fixture)
            run_command(common+['--rom',str(testrom)]+extra,folder/'emulator.log')
            # Exact duplicate frames add no information to the local review page.
            screenshots=[];seen=set()
            for p in sorted((folder/'captures').glob('*.png')):
                signature=digest(p.read_bytes())
                if signature not in seen:
                    seen.add(signature);screenshots.append(p.relative_to(run).as_posix())
            assert screenshots,'Emulador não produziu capturas.'
            report['resources'].append({'id':e['id'],'bytes':e['bytes'],'translation':translation,
                'status':'Execução concluída; revisão visual pendente','screenshots':screenshots,'source_hash':e['source_hash'],**({'headerless_context_scene':context_scene} if context_scene is not None else {})})
            previous[str(e['id'])]=e['source_hash']
            cache.parent.mkdir(parents=True,exist_ok=True)
            cache.write_text(json.dumps(previous,indent=2),encoding='utf-8')
            write_report(run,report)
        else:report['status']='Verificações automáticas concluídas; revisão visual pendente'
    except Exception as error:
        report['status']='falhou';report['error']=str(error)
        print('ERRO: '+str(error),flush=True)
    write_report(run,report)
    print(f'REPORT={run / "report.html"}',flush=True)
    return 1 if report['status']=='falhou' else 0

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rom',type=Path,required=True)
    parser.add_argument('--core',type=Path,required=True)
    parser.add_argument('--state',type=Path,required=True)
    parser.add_argument('--kind',choices=['story','battle'],default='battle')
    parser.add_argument('--scope',choices=['all','changed'],default='all')
    parser.add_argument('--count',type=int,default=3)
    parser.add_argument('--battle-frames',type=int,default=900,help='Single-run capture window; increase for multi-page resources')
    parser.add_argument('--cancel-file',type=Path)
    parser.add_argument('--resources',default='',help='Optional resource IDs/ranges, e.g. 738-779,783-785')
    args=parser.parse_args()
    try:sys.exit(execute(args))
    except (AssertionError,OSError) as error:print('ERRO: '+str(error),flush=True);sys.exit(1)
