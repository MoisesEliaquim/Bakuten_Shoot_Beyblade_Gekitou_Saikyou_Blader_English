"""Minimal local libretro host for reproducible mGBA screenshots and save states."""
import argparse
import ctypes as C
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--rom', type=Path, required=True)
parser.add_argument('--core', type=Path, required=True)
parser.add_argument('--output-dir', type=Path, required=True)
parser.add_argument('--capture-from', type=int, default=0)
parser.add_argument('--frames', type=int, default=600)
parser.add_argument('--load-state', type=Path)
parser.add_argument('--save-state', type=Path)
parser.add_argument('--buttons', default='')
parser.add_argument('--pulse', type=int, default=0)
parser.add_argument('--pulse-width', type=int, default=3)
parser.add_argument('--initial-buttons', default='')
parser.add_argument('--initial-frames', type=int, default=0)
parser.add_argument('--output', default='screen.png')
parser.add_argument('--dump-ram', type=Path)
parser.add_argument('--capture-every', type=int, default=0)
parser.add_argument('--test-battle-resource', type=int, help='Fixture only: inject a group-2 stream into the active battle renderer')
parser.add_argument('--test-battle-frame', type=int, default=270)
args = parser.parse_args()
OUTPUT=args.output_dir.resolve()
OUTPUT.mkdir(parents=True, exist_ok=True)
core = C.CDLL(str(args.core.resolve()))
ENV = C.CFUNCTYPE(C.c_bool, C.c_uint, C.c_void_p)
VIDEO = C.CFUNCTYPE(None, C.c_void_p, C.c_uint, C.c_uint, C.c_size_t)
AUDIO = C.CFUNCTYPE(None, C.c_int16, C.c_int16)
BATCH = C.CFUNCTYPE(C.c_size_t, C.c_void_p, C.c_size_t)
POLL = C.CFUNCTYPE(None)
INPUT = C.CFUNCTYPE(C.c_int16, C.c_uint, C.c_uint, C.c_uint, C.c_uint)
pixel_format = 0
frame = 0
last_frame = None
folder = C.create_string_buffer(str(OUTPUT).encode())
buttons = {'B': 0, 'SELECT': 2, 'START': 3, 'UP': 4, 'DOWN': 5, 'LEFT': 6, 'RIGHT': 7, 'A': 8, 'L': 10, 'R': 11}
pressed = {buttons[x] for x in args.buttons.upper().split(',') if x}
initial_pressed = {buttons[x] for x in args.initial_buttons.upper().split(',') if x}
ewram = None

class MemoryDescriptor(C.Structure):
    _fields_ = [('flags', C.c_uint64), ('ptr', C.c_void_p), ('offset', C.c_size_t),
                ('start', C.c_size_t), ('select', C.c_size_t), ('disconnect', C.c_size_t),
                ('length', C.c_size_t), ('addrspace', C.c_char_p)]

class MemoryMap(C.Structure):
    _fields_ = [('descriptors', C.POINTER(MemoryDescriptor)), ('count', C.c_uint)]

@ENV
def environment(command, pointer):
    global pixel_format, ewram
    command &= 0xFFFF
    if command == 36:
        mapping = C.cast(pointer, C.POINTER(MemoryMap)).contents
        for i in range(mapping.count):
            item = mapping.descriptors[i]
            if item.start == 0x02000000:
                ewram = item.ptr + item.offset
        return True
    if command == 10:
        pixel_format = C.cast(pointer, C.POINTER(C.c_int))[0]
        return True
    if command in (9, 30, 31):
        C.cast(pointer, C.POINTER(C.c_char_p))[0] = C.cast(folder, C.c_char_p)
        return True
    if command == 3:
        C.cast(pointer, C.POINTER(C.c_bool))[0] = False
        return True
    if command == 15:
        return False
    if command == 17:
        C.cast(pointer, C.POINTER(C.c_bool))[0] = False
        return True
    if command == 18:
        C.cast(pointer, C.POINTER(C.c_bool))[0] = False
        return True
    return command in (11, 16, 35)

@VIDEO
def video(pointer, width, height, pitch):
    global last_frame
    if not pointer:
        return
    last_frame = (C.string_at(pointer, pitch * height), width, height, pitch)

def decode_frame(snapshot):
    raw, width, height, pitch = snapshot
    if pixel_format == 1:
        return Image.frombytes('RGB', (width, height), raw, 'raw', 'BGRX', pitch)
    else:
        pixels = bytearray(width * height * 3)
        for y in range(height):
            for x in range(width):
                p = y*pitch+x*2
                value = raw[p] | raw[p+1] << 8
                r = (value >> (11 if pixel_format == 2 else 10)) & 31
                g = (value >> 5) & (63 if pixel_format == 2 else 31)
                b = value & 31
                q = (y*width+x)*3
                pixels[q:q+3] = bytes((r*255//31, g*255//(63 if pixel_format == 2 else 31), b*255//31))
        return Image.frombytes('RGB', (width, height), bytes(pixels))

@AUDIO
def audio(left, right):
    pass

@BATCH
def batch(pointer, frames):
    return frames

@POLL
def poll():
    pass

@INPUT
def input_state(port, device, index, button):
    return int(port == 0 and ((frame < args.initial_frames and button in initial_pressed) or (frame >= args.initial_frames and button in pressed and (not args.pulse or frame % args.pulse < args.pulse_width))))

class GameInfo(C.Structure):
    _fields_ = [('path', C.c_char_p), ('data', C.c_void_p), ('size', C.c_size_t), ('meta', C.c_char_p)]

for name, callback in [('environment', environment), ('video_refresh', video), ('audio_sample', audio),
                       ('audio_sample_batch', batch), ('input_poll', poll), ('input_state', input_state)]:
    function = getattr(core, 'retro_set_'+name)
    function.argtypes = [type(callback)]
    function(callback)
core.retro_init()
rom = args.rom.resolve()
rom_buffer = C.create_string_buffer(rom.read_bytes())
info = GameInfo(str(rom).encode(), C.cast(rom_buffer, C.c_void_p), rom.stat().st_size, None)
core.retro_load_game.argtypes = [C.POINTER(GameInfo)]
core.retro_load_game.restype = C.c_bool
assert core.retro_load_game(C.byref(info)), 'ROM load failed'
core.retro_serialize_size.restype = C.c_size_t
core.retro_serialize.argtypes = [C.c_void_p, C.c_size_t]
core.retro_serialize.restype = C.c_bool
core.retro_unserialize.argtypes = [C.c_void_p, C.c_size_t]
core.retro_unserialize.restype = C.c_bool
if args.load_state:
    state = C.create_string_buffer(args.load_state.read_bytes())
    assert core.retro_unserialize(state, len(state)-1)
core.retro_get_memory_size.argtypes = [C.c_uint]
core.retro_get_memory_size.restype = C.c_size_t
core.retro_get_memory_data.argtypes = [C.c_uint]
core.retro_get_memory_data.restype = C.c_void_p
for frame in range(args.frames):
    if args.test_battle_resource is not None and frame == args.test_battle_frame:
        import struct
        base=0x32AACC
        resource=base+struct.unpack_from('<I',rom.read_bytes(),base+4*args.test_battle_resource)[0]
        assert ewram and resource<len(rom_buffer)-1
        C.memmove(ewram+0x2820,struct.pack('<I',0x08000000+resource),4)
        C.memmove(ewram+0x2828,struct.pack('<IHH',0,0x40,0),8)
        C.memmove(ewram+0x2830,struct.pack('<H',1),2)
    core.retro_run()
    if args.capture_every and frame+1 >= args.capture_from and (frame+1) % args.capture_every == 0 and last_frame:
        capture_dir = OUTPUT / 'captures'
        capture_dir.mkdir(exist_ok=True)
        decode_frame(last_frame).save(capture_dir / f'{Path(args.output).stem}-{frame+1:05d}.png')
assert last_frame is not None, 'No video frames'
decode_frame(last_frame).save(OUTPUT / args.output)
if args.dump_ram:
    assert ewram
    args.dump_ram.write_bytes(C.string_at(ewram, 0x40000))
if args.save_state:
    size = core.retro_serialize_size()
    state = C.create_string_buffer(size)
    assert core.retro_serialize(state, size)
    args.save_state.write_bytes(state.raw)
core.retro_unload_game()
core.retro_deinit()
print(f'Emulated {args.frames} frames; pixel format {pixel_format}; screenshot {args.output}')
