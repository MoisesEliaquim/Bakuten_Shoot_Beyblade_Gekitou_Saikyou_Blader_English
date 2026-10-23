"""Relocate battle resources while preserving their non-text control stream."""
import json
import re
import struct
import textwrap

BASE=0x32AACC

def split_resource(data):
    tokens=[];pos=0;text=''
    def flush():
        nonlocal text
        if text: tokens.append(('text',text));text=''
    while pos+2<=len(data):
        pair=data[pos:pos+2]
        if pair in (b'FF',b'WF'):
            flush();tokens.append(('raw',data[pos:pos+4]));pos+=4
        elif pair==b'KK':text+='\n';pos+=2
        elif pair==b'PP':flush();tokens.append(('raw',pair));pos+=2
        elif pair==b'EE':
            flush();tokens.append(('raw',data[pos:]));return tokens
        elif pair in (b'N1',b'N2'):
            text+='{'+pair.decode()+'}';pos+=2
            # Battle names carry a suffix marker; preserve it with the placeholder.
            assert data[pos:pos+2]=='∝'.encode('cp932')
            pos+=2
        else:
            assert len(pair.decode('cp932'))==1, (pos,pair)
            text+=pair.decode('cp932');pos+=2
    raise AssertionError('Missing battle EE terminator')

def encode_page(text):
    lines=[]
    for line in text.split('\n'):
        lines.extend(textwrap.wrap(line,width=24,break_long_words=False,break_on_hyphens=False) or [''])
    assert len(lines)<=2, ('Battle page too long',text,lines)
    assert all(len(re.sub(r'\{N[12]\}','XXXXXXXX',line))<=24 for line in lines)
    result=bytearray()
    for i,line in enumerate(lines):
        if i:result+=b'KK'
        for fragment in re.split(r'(\{N[12]\})',line):
            if re.fullmatch(r'\{N[12]\}',fragment):
                # The optional original suffix marker appends Japanese "kun".
                # English retains the runtime name without that honorific.
                result+=fragment[1:-1].encode()
            else:result+=''.join('　' if c==' ' else '’' if c=="'" else chr(ord(c)+0xFEE0) if '!'<=c<='~' else c for c in fragment).encode('cp932')
    return result

def apply_battle(original,out,path):
    entries=json.loads(path.read_text('utf-8'));cursor=0x500000;manifest=[]
    # Move the five-cell reaction timer from BG1 rows 15-16 to rows 5-6.
    # Update drawing, individual-cell clearing, and whole-bar clearing together.
    for offset in (0x19AD4,0x19BA0,0x19C08):
        assert struct.unpack_from('<I',original,offset)[0]==0x06000BF6
        struct.pack_into('<I',out,offset,0x06000976)
    # The old clearing tile was the dialogue's blue background. At the new
    # arena position, clear with the existing transparent tile instead.
    for call,hook,load in [(0x19B6C,0x400080,0x4F00),(0x19BAE,0x400088,0x4800)]:
        expected=bytes.fromhex('c8277f03' if call==0x19B6C else 'c8204003')
        assert original[call:call+4]==expected
        payload=struct.pack('<HHI',load,0x4770,0xF3FF0000)
        assert all(v==255 for v in out[hook:hook+len(payload)])
        out[hook:hook+len(payload)]=payload
        delta=hook-(call+4)
        struct.pack_into('<HH',out,call,0xF000|((delta>>12)&0x7FF),0xF800|((delta>>1)&0x7FF))
    # The battle interpreter has its own 28-byte line buffer and font selection.
    for offset,before,after in [(0x1E8E6,0xB089,0xB091),(0x1EB0A,0xB009,0xB011)]:
        assert struct.unpack_from('<H',original,offset)[0]==before
        struct.pack_into('<H',out,offset,after)
    hook=0x400040
    instructions=[0x6832,0x0D92,0x2A21,0xD101,0x2201,0xE000,0x2200,0x2301,0x4770]
    payload=struct.pack('<'+'H'*len(instructions),*instructions)
    assert all(v==255 for v in out[hook:hook+len(payload)])
    out[hook:hook+len(payload)]=payload
    call=0x1EB02
    assert original[call:call+4]==bytes.fromhex('00220123')
    delta=hook-(call+4)
    struct.pack_into('<HH',out,call,0xF000|((delta>>12)&0x7FF),0xF800|((delta>>1)&0x7FF))
    for entry in entries:
        index=entry['resource'];start=BASE+struct.unpack_from('<I',original,BASE+4*index)[0]
        end=BASE+struct.unpack_from('<I',original,BASE+4*(index+1))[0]
        assert BASE<start<end<len(original)
        tokens=split_resource(original[start:end]);pages=[t for kind,t in tokens if kind=='text' and t.strip()]
        assert pages==entry['original_pages'],index
        assert len(pages)==len(entry['english_pages']),index
        replacements=iter(entry['english_pages']);payload=bytearray()
        for kind,value in tokens:
            if kind=='raw':payload+=value
            elif not value.strip():payload+=value.encode('cp932')
            else:
                translated=next(replacements)
                assert re.findall(r'\{N[12]\}',value)==re.findall(r'\{N[12]\}',translated),index
                payload+=encode_page(translated)
        assert cursor+len(payload)<0x7F0000
        assert all(v==255 for v in out[cursor:cursor+len(payload)])
        out[cursor:cursor+len(payload)]=payload
        struct.pack_into('<I',out,BASE+4*index,cursor-BASE)
        manifest.append({'resource':index,'old_offset':hex(start),'new_offset':hex(cursor),'bytes':len(payload)})
        cursor=(cursor+len(payload)+3)&~3
    return manifest
