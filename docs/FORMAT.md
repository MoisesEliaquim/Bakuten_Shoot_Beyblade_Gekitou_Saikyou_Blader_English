# AHEJ text and font notes

All file offsets below apply only to the exact Japanese ROM hash in the README. CPU ROM addresses add `0x08000000` to file offsets.

## Resource tables

The resource loader at `0x08002B30` reads a group pointer, then a 32-bit little-endian offset relative to the group's base. The root table is at file offset `0x120AC8`.

| Group | Base file offset | Notes |
| --- | --- | --- |
| 1 | `0x31CD4C` | Story resources, including the translated scenes |
| 2 | `0x32AACC` | Other dialogue resources; not fully mapped |

For group 1, the entry for scene `n` is at `0x31CD4C + 4*n`. The target is the group base plus the stored offset. Resource boundaries must not be inferred solely from a text search.

## Text and commands

Text uses two-byte CP932/Shift-JIS characters. The game's fullwidth Latin characters are encoded as two bytes too. The English builder converts ordinary Latin text into those character codes; it does not write ASCII dialogue directly.

| Bytes | Visible marker | Observed use |
| --- | --- | --- |
| `46 46` | `FF` | Speaker record, followed by a two-byte little-endian ID |
| `4B 4B` | `KK` | Line transition in the tested story interpreter |
| `50 50` | `PP` | Page transition in the tested story interpreter |
| `57 57` | `WW` | End/wait-related marker; preserve its context |
| `45 45` | `EE` | Scene termination in the tested combinations |

The builder currently accepts scenes ending in `WWEE` and preserves speaker order. It intentionally rejects other command types. `N1` occurs in untranslated scenes as a runtime name-related command; its full semantics and safe wrapping are not implemented. These observations are not a complete specification for all game interpreters.

## The `.tbl` file

`tables/beyblade-ahej.tbl` maps hex byte pairs in file order to CP932 characters and six readable command markers. It is UTF-8 and contains 7,342 entries. Editors differ in table syntax and how they display spaces or duplicate character mappings; test the editor's interpretation before writing bytes.

A `.tbl` cannot express the complete `FF` parameter structure, variable substitutions, pointer tables, or event logic. Use it for inspection; use the validated scripts for building.

## Font and buffer changes

The game contains a narrow renderer at `0x0800AC2C` and a wide renderer at `0x0800AB7C`. The tested narrow path uses an 8-pixel tile advance and supports the translated Latin glyphs.

The story interpreter begins at `0x0800FA98`. Its original temporary string buffer is too small for a 24-character line. The patch increases the stack allocation by 32 bytes and shifts the following stack locals. Outgoing call arguments are not shifted.

A hook at file offset `0x400000` selects narrow mode for dialogue streams in `0x08400000–0x087FFFFF`; original streams retain their font mode. This range check is specific to the current memory layout. Any future allocator must preserve or revise it deliberately.

Current allocations:

| File range | Purpose |
| --- | --- |
| `0x410000` up to `0x7F0000` | Relocated English story resources; the builder checks for overlap |
| `0x400000` onward | Small font-mode hook, separate from the dialogue pool |
| `0x7F0000` up to `0x800000` | Relocated UI labels with a ROM-capacity check |

The resulting ROM is padded to 8 MiB. Changing the emulator window size does not change the GBA's 240×160 internal framebuffer.
