# Progress and validation

## Current version: 1.48 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **816 UI strings**. Centers the Beyblade catalog title within its existing Japanese title field using the original narrow font. UI source inventory remains 816 strings.

The title uses the original 15-character fixed field. The portable build and independent IPS verification passed once (2260 records). The catalog attribute labels visible in the right panel are drawn outside the pointer-backed UI strings; their graphics/code source is still under investigation, so this release does not claim those labels are translated.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.47 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **816 UI strings**. Shortens the Beyblade Select title to Beyblade and replaces remaining character surname-plus-given-name aliases with first names: Kai, Max, Masamune, Kaoru, Kiyoshi; the role label Mizuhara Chichi is shortened to Dad. UI source coverage remains 816 strings.

All 11 changed source strings, Japanese source bytes, pointer targets, and fixed display capacities passed. Private and portable builds completed; independent IPS verification passed once (2263 records). Visual review remains pending: available UI states contain cached Japanese labels and cannot confirm these changes.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.46 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **816 UI strings**. Corrects six pointer-backed character labels to first names (Rei, Takao, Daichi) and shortens the Beyblade Select title to Beyblade Sel. UI source coverage remains 816 strings.

All seven changed source strings, Japanese source bytes, pointer targets, and fixed display capacities passed. Private and portable builders completed; independent IPS verification passed once (2263 records). Existing mGBA UI states retain Japanese names in RAM, so attempted captures do not validate the changed labels; visual review remains pending a fresh state at the target screens.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.45 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **816 UI strings**. Adds five remaining pointer-backed Metal Change catalog variants as MChg; common variants were already translated. UI source coverage reaches 816 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2263 records). Three selected variants (0x43D1C, 0x43D30, 0x43DA8) rendered legibly in 360-frame narrow-font guide-field fixtures. The field did not preserve marker suffixes, so this review confirms text rendering only; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.44 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **811 UI strings**. Adds five remaining pointer-backed Metal Ball catalog variants as MtBall; three common variants were already translated. UI source coverage reaches 811 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2258 records). Three selected variants (0x43C6C, 0x43C80, 0x43CF8) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed FK for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.43 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **806 UI strings**. Adds five remaining pointer-backed Griffolion catalog variants as Griff; three common variants were already translated. UI source coverage reaches 806 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2248 records). Three selected variants (0x43764, 0x43778, 0x437F0) rendered legibly in 360-frame narrow-font guide-field fixtures; the field showed PK on two and BK on one. Natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.42 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **801 UI strings**. Adds five remaining pointer-backed Magnet Flat catalog variants as MagFlat; three common variants were already translated. UI source coverage reaches 801 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2243 records). Three selected variants (0x436B4, 0x436C8, 0x43740) rendered legibly in 360-frame narrow-font guide-field fixtures; two showed FK and one BK. Natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.41 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **796 UI strings**. Adds five remaining pointer-backed G-Special catalog variants as G-Spec; three common variants were already translated. UI source coverage reaches 796 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2238 records). Three selected variants (0x43604, 0x43618, 0x43690) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed PK for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.40 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **791 UI strings**. Adds five remaining pointer-backed Earth Wing catalog variants as EarthW; the three common variants were already translated. UI source coverage reaches 791 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2233 records). Three selected variants (0x43554, 0x43568, 0x435E0) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed PK for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.39 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **786 UI strings**. Adds four remaining pointer-backed Reverse Dragon catalog variants as RevDrgn; its standard variants were already translated. UI source coverage reaches 786 strings; the wider inventory remains incomplete.

All four added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2228 records). Three selected variants (0x434B4, 0x434E4, 0x434FC) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.38 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **782 UI strings**. Adds four missing pointer-backed Double Wing catalog variants as DblWing; two common variants were already translated. UI source coverage reaches 782 strings; the wider inventory remains incomplete.

All four added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2224 records). Three selected variants (0x433FC, 0x43438, 0x43460) rendered legibly in 360-frame narrow-font guide-field fixtures with GR, FD, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.37 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **778 UI strings**. Adds five remaining pointer-backed Tiger DF catalog variants as TigrDF; the arrow variant was already translated. UI source coverage reaches 778 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2220 records). Three selected variants (0x43388, 0x4339C, 0x433D8) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed YL for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.36 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **773 UI strings**. Adds five missing pointer-backed Cross Spike catalog variants as XSpike; the two common variants were already translated. UI source coverage reaches 773 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2215 records). Three selected variants (0x432EC, 0x43314, 0x43350) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed the same LG suffix for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.35 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **768 UI strings**. Adds five remaining pointer-backed Upper DRG catalog variants as UpprDRG; the standard variant was already translated. UI source coverage reaches 768 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2210 records). Three selected variants (0x43278, 0x4328C, 0x432C8) rendered legibly in 360-frame narrow-font guide-field fixtures with FK, BL, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.34 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **763 UI strings**. Adds four remaining pointer-backed Smash TTL catalog variants as SmashT; two common variants were already translated. UI source coverage reaches 763 strings; the wider inventory remains incomplete.

All four added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2205 records). Three selected variants (0x431F0, 0x43208, 0x43238) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed BL for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.33 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **759 UI strings**. Adds four remaining pointer-backed Night Crows catalog variants as N.Crow; two common variants were already translated. UI source coverage reaches 759 strings; the wider inventory remains incomplete.

All four added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2201 records). Three selected variants (0x43160, 0x43174, 0x4319C) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed BL for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.32 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **755 UI strings**. Adds four missing pointer-backed Triple Wing catalog variants as TriWing; two common variants were already translated. UI source coverage reaches 755 strings; the wider inventory remains incomplete.

All four added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2197 records). Three selected variants (0x430C4, 0x430DC, 0x4310C) rendered legibly in 360-frame narrow-font guide-field fixtures with BL, FD, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.31 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **751 UI strings**. Adds five missing pointer-backed Star Shape catalog variants as StarShp; the standard variant was already translated. UI source coverage reaches 751 strings; the wider inventory remains incomplete.

All five added source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2193 records). Three selected variants (0x4300C, 0x43034, 0x43070) rendered legibly in 360-frame narrow-font guide-field fixtures with GR, BL, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.30 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **746 UI strings**. Adds six pointer-backed Scissor Cutter catalog variants as ScisCut, preserving original category markers. UI source coverage reaches 746 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2188 records). Three selected variants (0x42F84, 0x42FD4, 0x42FE8) rendered legibly in 360-frame narrow-font guide-field fixtures with GR, FK, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.29 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **740 UI strings**. Adds six pointer-backed Turtle SVV catalog variants as TurtSVV, preserving original category markers. UI source coverage reaches 740 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2182 records). Three selected variants (0x42EFC, 0x42F4C, 0x42F60) rendered legibly in 360-frame narrow-font guide-field fixtures with GR, OR, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.28 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **734 UI strings**. Adds six pointer-backed Wing Cutter catalog variants as WngCut, preserving original category markers. UI source coverage reaches 734 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2176 records). Three selected variants (0x42E58, 0x42E88, 0x42ED0) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed GR for all three and did not confirm marker differences; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.27 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **728 UI strings**. Adds six pointer-backed Max Shield catalog variants as MaxShld, preserving original category markers. UI source coverage reaches 728 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2170 records). Three selected variants (0x42DB4, 0x42DE4, 0x42E2C) rendered legibly in 360-frame narrow-font guide-field fixtures, including distinct FK, BL, and WH suffixes; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.26 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **722 UI strings**. Adds six pointer-backed War Monkey catalog variants as WarMky, preserving original category markers. UI source coverage reaches 722 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2164 records). Three selected variants (0x42D2C, 0x42D54, 0x42D90) rendered legibly in 360-frame narrow-font guide-field fixtures. The field showed the same category suffix for the selected variants; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.25 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **716 UI strings**. Adds six pointer-backed War Bear catalog variants as W.Bear, preserving original category markers. UI source coverage reaches 716 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2158 records). Three selected variants (0x42CA4, 0x42CCC, 0x42CE0) rendered legibly in 360-frame narrow-font guide-field fixtures. The fixture field displayed the same GR suffix for the selected variants; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.24 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **710 UI strings**. Adds six pointer-backed Roller Attack catalog variants as RollAtk, preserving original category markers. UI source coverage reaches 710 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2152 records). Three selected variants (0x42B7C, 0x42BAC, 0x42BF4) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.23 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **704 UI strings**. Adds six pointer-backed Spark Attack catalog variants as SpkAtk, preserving original category markers. UI source coverage reaches 704 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2146 records). Three selected variants (0x42AD8, 0x42B08, 0x42B50) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.22 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **698 UI strings**. Adds six pointer-backed Bound Attack catalog variants as BndAtk, preserving original category markers. UI source coverage reaches 698 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2140 records). Three selected variants (0x42A34, 0x42A4C, 0x42AAC) rendered legibly in 360-frame narrow-font guide-field fixtures; the rare marker variants showed the same category label in this field, and natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.21 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **692 UI strings**. Adds six pointer-backed Reverse Wolf catalog variants as RevWolf, preserving original category markers. UI source coverage reaches 692 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. Portable build and independent IPS verification passed once (2134 records). Three selected variants (0x429AC, 0x429D4, 0x42A10) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.20 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **686 UI strings**. Adds six pointer-backed Whale CRS catalog variants as WhlCRS, preserving original category markers. UI source coverage reaches 686 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. The portable build and independent IPS verification passed once (2128 IPS records). Three selected variants (0x42924, 0x4294C, 0x42988) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.19 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **680 UI strings**. Adds six pointer-backed Wing DF catalog variants with compact spelling; original category markers are preserved. UI source coverage reaches 680 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. The portable build and independent IPS verification passed once (2122 IPS records). Three selected variants (0x4289C, 0x428C4, 0x428EC) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.18 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **674 UI strings**. Adds six pointer-backed Wing AT catalog variants with compact spelling; original category markers are preserved. UI source coverage reaches 674 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. The portable build and independent IPS verification passed once (2116 IPS records). Three selected variants (0x42814, 0x4283C, 0x42878) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.17 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **668 UI strings**. Adds six pointer-backed Dual Dragon catalog variants with compact spelling; original category markers are preserved. UI source coverage reaches 668 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. The portable build and independent IPS verification passed once (2110 IPS records). Three selected variants (0x42770, 0x427A0, 0x427E8) rendered legibly in 360-frame narrow-font guide-field fixtures; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.16 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **662 UI strings**. Adds six pointer-backed Flame Wing catalog variants with compact spelling; original graphic marker bytes are preserved. UI source coverage reaches 662 strings; the wider inventory remains incomplete.

All six source strings, pointer targets, marker bytes, and fixed display capacities passed. The portable build and independent IPS verification passed once (2104 IPS records). The local QA runner does not support UI catalog fixtures; no emulator or natural catalog-placement review was run.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.15 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **656 UI strings**. Adds twelve pointer-backed catalog names: five Eight Spike variants and seven Cross Fang variants. Original graphic marker bytes are preserved. UI source coverage reaches 656 strings; the wider inventory remains incomplete.

The first build caught missing source-byte metadata for graphic marker suffixes. After recording the exact Japanese and English marker bytes, all twelve source strings, pointer targets, and fixed capacities passed. The portable build and independent IPS verification passed once (2098 IPS records). The local QA runner does not support UI catalog fixtures; no emulator or natural catalog-placement review was run.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.14 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **644 UI strings**. Adds sixteen localized credits labels for staff names, Takara, and the CoroCoro Comic editorial department. UI source coverage reaches 644 strings; the full inventory remains incomplete. Staff names use compact phonetic romanizations because the source gives kana only.

All sixteen source strings and pointer targets matched the Japanese ROM; fixed display-capacity checks passed. The portable build and independent IPS verification passed once (2087 IPS records). The local QA runner does not support credit/UI resources, so no emulator or natural credits-screen review was run.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.13 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **628 UI strings**. Adds eight pointer-backed catalog variants for Eight Attacker and Cross Griffin, preserving the original category-marker bytes. UI source coverage reaches 628 strings; the wider catalog inventory remains incomplete.

The eight source strings, ROM byte sequences, pointers, and fixed display capacities passed checks. The portable build and independent IPS verification passed once (2070 IPS records). The local QA runner supports story and battle resources, not UI catalog fixtures; no emulator or natural catalog-placement review was run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.12 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **620 UI strings**. Adds ten pointer-backed UI labels: the Old Man and Daitenji aliases, plus missing Wing Blade and Great Dragon catalog variants.

The ten source strings, ROM byte sequences, and pointer targets were verified. All labels passed fixed-capacity checks. The portable build and independent IPS verification passed once (2062 IPS records). The local story/battle QA runner does not accept UI resources; no emulator or natural menu-placement review was run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.11 — experimental, local draft

The editable sources contain **585 speeches in 307 scenes (308–616)** and **610 UI strings**. Adds the remaining two café prompts (scenes 326–327), with short wording for the quick headerless exchange.

The local QA app executed both scenes and the build/IPS checks passed. Manual review of the larger scene 327 showed that the dialogue advances quickly: the longer “May I help you?” and first abbreviation did not finish before the next event. The final line was shortened to “Help?” and passed portable byte/layout/build/IPS checks. Scene 327 reached the three-run limit, so the final wording was not re-run in the emulator. Scene fixtures do not confirm natural triggers.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.10 — experimental, local draft

The editable sources contain **583 speeches in 305 scenes (308–616)** and **610 UI strings**. Adds two café service prompts (scenes 320–321). The longer wording in scene 321 was shortened after local visual review.

The local QA app executed both scenes and the automatic build/IPS check passed. Manual review of the larger scene 321 found that its long wording advanced before the reveal completed. The line was shortened to “Ready to order?” and then passed the portable byte/layout/build/IPS checks. Scene 321 reached the three-run emulator limit, so the corrected wording was not re-run in the emulator. Scene fixtures do not confirm natural triggers.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.09 — experimental, local draft

The editable sources contain **581 speeches in 303 scenes (308–616)** and **610 UI strings**. Adds four short café prompts (scenes 313–316) that were missing from the selected pre-opening dialogue block.

The local QA app built the ROM and independently verified the IPS once, then ran all four scenes. Manual review of the largest scene (315) confirmed both pages and the complete English text. Scenes use the original EE-only ending; the dialogue builder now preserves either EE or WWEE. Temporary scene-pointer fixtures do not confirm natural triggers or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.08 — experimental, local draft

The editable sources contain **577 speeches in 299 scenes (308–616)** and **610 UI strings**. Adds the four remaining compact catalog variants for Eight Wide, preserving the original marker bytes. UI source coverage remains incomplete.

All four Japanese byte sequences and pointer targets were checked against the original ROM; abbreviated labels fit fixed display capacities. Portable build and independent IPS verification passed once. Three largest labels (0x447BC, 0x447D0, 0x447E4) rendered legibly in the narrow font after exiting and re-entering the guide. The temporary guide-field fixture confirms rendering and fit, not natural catalog placement.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

A cumulative static audit of the v1.08 ROM passed for all 610 UI strings and 299 dialogue scenes / 577 speeches, checking source bytes, pointers, capacities, command layout, and exact output bytes. The audit did not rebuild or repeat IPS verification. A 30-sample emulator review across v93-v99 and v106-v108 confirmed narrow-font rendering and fit in temporary guide-field fixtures. An 18-sample review across v100-v105 displayed the target dialogue in timed capture frames. Natural catalog placement and natural dialogue triggers remain unconfirmed.

## Historical snapshot: 1.07 — experimental, local draft

The editable sources contain **577 speeches in 299 scenes (308–616)** and **606 UI strings**. Adds eight compact catalog variants for Eight Balance and Eight Heavy, preserving their original marker bytes. UI source coverage remains incomplete.

All eight Japanese byte sequences and pointer targets were checked against the original ROM; abbreviated labels fit fixed display capacities. Portable build and independent IPS verification passed once. Three largest labels (0x446AC, 0x446C0, 0x44734) rendered legibly in the narrow font in the guide-field fixture on v1.08; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.06 — experimental, local draft

The editable sources contain **577 speeches in 299 scenes (308–616)** and **598 UI strings**. Adds eight pointer-backed catalog variants for Heavy and Balance. The original category markers are retained; UI coverage remains incomplete.

All eight Japanese byte sequences and pointer targets were checked against the original ROM; encoded labels fit their fixed display capacities. Portable build and independent IPS verification passed on the third attempt. Three largest labels (0x44638, 0x44648, 0x44658) rendered legibly in the narrow font in the guide-field fixture on v1.08; natural catalog placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.05 — experimental, local draft

The editable sources contain **577 speeches in 299 scenes (308–616)** and **590 UI strings**. Part 6/6 completes the selected earlier dialogue-table block with five numbered names. Across six parts, 35 scenes were added; mixed-format scene 312 remains unsupported. Current totals reach 577 speeches across 299 translated dialogue scenes, including non-narrative resources.

Portable build and independent IPS verification passed once (2022 records). Three largest resources (349, 350, 352) were confirmed in timed captures with the expected names and portrait context. The scene-pointer fixture does not confirm a natural trigger or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.04 — experimental, local draft

The editable sources contain **572 speeches in 294 scenes (308–616)** and **590 UI strings**. Part 5/6 translates six numbered character-name entries, IDs 10–16. Current totals reach 572 speeches across 294 translated dialogue scenes; counts include non-narrative resources.

Portable build and independent IPS verification passed once (2017 records). Three largest resources (342, 346, 347) were confirmed in timed captures with the expected names and portrait context. The scene-pointer fixture does not confirm a natural trigger or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.03 — experimental, local draft

The editable sources contain **566 speeches in 288 scenes (308–616)** and **590 UI strings**. Part 4/6 translates six numbered character-name entries, IDs 04–09. Current totals reach 566 speeches across 288 translated dialogue scenes; counts include non-narrative resources.

Portable build and independent IPS verification passed once (2013 records). Three largest resources (337, 339, 340) were confirmed in timed captures with the expected names and portrait context. The scene-pointer fixture does not confirm a natural trigger or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.02 — experimental, local draft

The editable sources contain **560 speeches in 282 scenes (308–616)** and **590 UI strings**. Part 3/6 adds two café lines and four numbered character-name entries. Current totals reach 560 speeches across 282 translated dialogue scenes; the count includes non-narrative resources.

The portable build and independent IPS verification passed once (2007 records). Three largest resources (330, 331, 332) were confirmed in timed captures: both pages of the caramel line, the iced-coffee line, and “00: Daichi” with Daichi’s portrait. The scene-pointer fixture does not confirm natural triggers or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.01 — experimental, local draft

The editable sources contain **554 speeches in 276 scenes (308–616)** and **590 UI strings**. Part 2/6 translates six café remarks from the earlier dialogue table. Current totals reach 554 speeches across 276 translated scenes; this count includes non-narrative dialogue resources.

One source edit replaced unsupported yen currency glyph with “180 yen”; the corrected portable build and independent IPS verification passed once (2000 records). Three largest resources (322, 324, 328) were confirmed in timed captures with the expected café lines. The scene-pointer fixture does not confirm natural triggers or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 1.00 — experimental, local draft

The editable sources contain **548 speeches in 270 scenes (308–616)** and **590 UI strings**. Part 1/6 translates six eligible scenes from the earlier dialogue table: scenario tests, café remarks, and dialogue. Current totals reach 548 speeches across 270 translated scenes. Mixed-format scene 312 remains unsupported and was excluded.

All new scene pointers, command streams, and speaker IDs passed the portable build; IPS verification passed once with 1994 records. Three largest resources (309, 318, 319) were confirmed across timed captures; the two longer lines span multiple pages. The first two build attempts failed on unsupported mixed-format scene 312 and a speaker mismatch in scene 319; corrected sources passed on the third and final allowed attempt. The scene-pointer fixture does not confirm natural triggers or full-game behavior.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.99 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **590 UI strings**. Part 6/6 completes the six-part alias batch with eight entries for Rei, Kai, Takao, and Daichi. UI source coverage reaches 590 strings; the full UI inventory remains incomplete.

All eight source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1988 IPS records). Three representative strings were rendered legibly in the narrow font in temporary guide-field fixtures; natural placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.98 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **582 UI strings**. Part 5/6 adds five aliases for Akira, Nobuo, Max, and Rei. UI source coverage reaches 582 strings; inventory remains incomplete.

All five source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1980 IPS records). Three representative strings were rendered legibly in the narrow font in temporary guide-field fixtures; natural placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.97 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **577 UI strings**. Part 4/6 adds five aliases for Mao, Rai, Yuri, Ralf, and Michael. UI source coverage reaches 577 strings; inventory remains incomplete.

All five source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1975 IPS records). Three representative strings were rendered legibly in the narrow font in temporary guide-field fixtures; natural placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.96 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **572 UI strings**. Part 3/6 adds five aliases for Professor, Masamune, Kaoru, and Kiki. UI source coverage reaches 572 strings; inventory remains incomplete.

All five source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1970 IPS records). Three representative strings were rendered legibly in the narrow font in temporary guide-field fixtures; natural placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.95 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **567 UI strings**. Part 2/6 adds five aliases for Suzuka, Tsukuba, and the Blader DJ title. UI source coverage reaches 567 strings; inventory remains incomplete.

All five source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1965 IPS records). Three representative strings were rendered legibly in the narrow font in temporary guide-field fixtures; natural placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.94 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **562 UI strings**. Adds five pointer-backed aliases for Grandpa, BBA, Daitenji, and Hiruta. UI source coverage reaches 562 strings; catalog inventory remains incomplete.

All five source strings and pointer targets matched the Japanese ROM byte-for-byte; fixed display capacities passed. Portable build and independent IPS verification passed once (1960 IPS records). Three larger aliases were rendered legibly in the narrow font in temporary guide-field fixtures; natural alias placement remains unconfirmed.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.93 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **557 UI strings**. Adds four pointer-backed catalog variants for Eight Heavy and Eight Wide. UI source coverage reaches 557 strings; the catalog inventory remains incomplete.

All four Japanese source strings and pointer targets were checked byte-for-byte; fixed display capacities passed. The portable build and independent IPS verification passed once (1955 IPS records). Three representative labels were rendered legibly in the narrow font after exiting and re-entering the guide. The temporary fixture confirms rendering and fit, not natural catalog placement. No battle or story samples were run.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.92 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **553 UI strings**. Corrects two truncated Spark catalog labels from “Spar” to “Spk” at 0x4450C and 0x4451C. The source still contains 553 UI strings; catalog inventory remains incomplete.

A temporary pointer fixture rendered all 60 catalog strings added in v0.86–v0.91 in the existing guide category field; both corrected strings were then rendered again. This confirms narrow-font text rendering in that field, not natural catalog placement: the available guide state has no catalog data. The visual pass found the ambiguous “Spar” abbreviation. Fixed-capacity and pointer checks passed. Portable build and independent IPS verification passed once; no emulator test was repeated for unrelated strings.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.91 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **553 UI strings**. Adds ten byte-verified catalog variants for Spark, Wide, Heavy, Balance, Eight Balance, and Eight Heavy. UI source coverage reaches 553 strings; the catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Verified attribute markers are retained. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.90 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **543 UI strings**. Adds ten byte-verified part labels and variants for The Weight, Wing Slave, Ten Wide, Heavy Attack, Wide DF, and Spark. UI source coverage reaches 543 strings; the catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Attribute markers with verified source encoding are retained. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.89 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **533 UI strings**. Adds ten byte-verified catalog variants for SG Semi Flat, SG Flat, SG Sharp, and Storm Grip. UI source coverage reaches 533 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.88 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **523 UI strings**. Adds ten byte-verified catalog variants for Phantom GRP, Spiral CH, Metal Ball, and Metal Change. UI source coverage reaches 523 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.87 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **513 UI strings**. Adds ten byte-verified catalog variants for Metal Sting, Bearing, Auto Change, and SG Semi Flat. UI source coverage reaches 513 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.86 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **503 UI strings**. Adds ten byte-verified catalog variants for Fortress, FA Clutch, Flame Change, and Phantom GRP. UI source coverage reaches 503 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.85 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **493 UI strings**. Adds ten byte-verified catalog variants for Magnetic Flat, Griffolion, Jumping, and Fortress. UI source coverage reaches 493 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.84 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **483 UI strings**. Adds ten byte-verified variants for Double Wing, Reverse Dragon, Earth Wing, and G-Special. UI source coverage reaches 483 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; no emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.83 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **473 UI strings**. Adds ten byte-verified catalog variants for Star Shape, Triple Wing, Night Crows, Smash TTL, Upper DRG, Cross Spike, and Tiger DF. UI source coverage reaches 473 strings; catalog inventory remains incomplete.

All ten pointer-backed source strings match the Japanese ROM byte-for-byte and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review of the UI remains deferred; the available encyclopedia state opens Upper DRG with no data, not Great Edge.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.82 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **463 UI strings**. Adds nine byte-matched catalog variants for Wing Blade, Great Dragon, Eight Attacker, Cross Griffin, and Eight Spike. Japanese stat markers with verified source encoding are retained. UI source coverage reaches 463 strings; catalog inventory remains incomplete.

The first build identified six CSV candidates with suffix text that did not match ROM bytes; those entries were removed. The corrected batch contains nine byte-for-byte verified additions, passes fixed display-capacity checks, and passed portable build plus independent IPS verification once. Two manual emulator runs used the available encyclopedia state, but it opened Upper DRG / No data, not Great Edge. The target entry was not visually reviewed; the user asked to continue without a capture.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.81 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **454 UI strings**. Adds nine remaining credits entries for Fuyuki, Hoshi, Director, Kadowaki, Product Manager, Otaka, Producer, Kidani, and Executive Producer. UI source coverage reaches 454 strings; credits inventory remains incomplete.

All nine pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.80 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **445 UI strings**. Adds ten compact credits entries for Kaneda, graphic design, Goto, Horii, Seguchi, Tanaka, Hirasawa, Takabatake, programming, and Yamagishi. UI source coverage reaches 445 strings; credits inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.79 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **435 UI strings**. Adds ten compact credits entries for special thanks, composition, sound direction, and staff names. UI source coverage reaches 435 strings; credits inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.78 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **425 UI strings**. Adds ten compact main-character and Beyblade labels, including Draciel, Driger, Dranzer, Dragoon, Mizuhara Max, Kai, Takao, and Daichi. UI source coverage reaches 425 strings; name inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.77 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **415 UI strings**. Adds ten compact character and Beyblade names, including Chizan Masamune, Pegasion, Amou Kaoru, Galman, Galux, Galon, Wolborg, Griffolion, and Trygle. UI source coverage reaches 415 strings; name inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.76 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **405 UI strings**. Adds ten compact Beyblade and character labels, including Kids Dragoon, Boosters 2–5, Mizuhara’s father, Grandpa, Blader DJ, Professor, and Masamune. UI source coverage reaches 405 strings; name inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.75 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **395 UI strings**. Adds three remaining compact weight-disk descriptions for the eight-sided disk, centrifugal endurance boost, and wide disk. UI source coverage reaches 395 strings; the interface inventory remains incomplete.

All three new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.74 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **392 UI strings**. Adds nine weight-disk descriptions and translates the development-staff heading. UI source coverage reaches 392 strings; guide and credits inventory remain incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.73 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **382 UI strings**. Adds ten weight-disk guide descriptions covering rubber shafts, phantom and anchor disks, speed and weight, endurance, ten-sided design, attack/defense, and mass. UI source coverage reaches 382 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.72 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **372 UI strings**. Adds ten blade-base guide entries covering bearings, auto-change, flat balance, attack mode, rapid movement, endurance, friction, and grip. UI source coverage reaches 372 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.71 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **362 UI strings**. Adds ten blade-base and sharp-disk guide descriptions about grip, defense mode, change gimmicks, endurance, dual balls, attack/endurance, and metal components. UI source coverage reaches 362 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.70 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **352 UI strings**. Adds ten compact blade-base guide descriptions covering the original base, transformation design, fierce attacks, Jumping and Oil Ball systems, auto endurance change, spin power, three modes, and speed. UI source coverage reaches 352 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.69 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **342 UI strings**. Adds ten compact blade-base guide entries covering all-round balance, variable-function attack rings, multi-balance, phantom and high-performance bases, Kaoru’s base, endurance, new features, and neodymium. UI source coverage reaches 342 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.68 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **332 UI strings**. Adds ten compact attack-ring guide entries covering Night Claws, balance type, Smash attacks, upper attacks, spike cutters, deflection, and spear-shaped rings. UI source coverage reaches 332 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.67 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **322 UI strings**. Adds ten compact guide descriptions for wing cutters, four and three-wing designs, slicing attacks, sickle blades, high-level defense, star-shaped rings, and balance. UI source coverage reaches 322 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.66 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **312 UI strings**. Adds ten short equipment-guide descriptions covering War Lion comparison, free switching and spinning, attack range, double wings, ironclad defense, shell spikes, and balance. UI source coverage reaches 312 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.65 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **302 UI strings**. Adds ten compact Beyblade guide descriptions about attack and defense compatibility, rearranging attack frames, bounce, Spark Disc, deflecting attacks, roller effects, and Mao’s ring. UI source coverage reaches 302 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.64 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **292 UI strings**. Adds ten compact guide descriptions covering stability, spikes, attack and defense balance, defensive design, materials, and wing systems. UI source coverage reaches 292 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.63 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **282 UI strings**. Adds ten compact attack-ring guide descriptions, including Phantom Ring, Eerie Lit, Wings Open, Smash, 8 Wings, and Attack Ring. UI source coverage reaches 282 strings; guide inventory remains incomplete.

All ten new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.62 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **272 UI strings**. Adds six compact attack names to the Beyblade guide: Storm Shoot, Screw Shoot, Spark Barrier, Thunder Survive, Thunder Crunch, and Thunder Saber. UI source coverage reaches 272 strings; guide inventory remains incomplete.

All six new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.61 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **266 UI strings**. Adds ten concise guide and move names for the Tiger and Fire lines, including Tiger Fang, Tiger Claw, Spin Fire Bomb, Vanishing Shadow, Storm Attack, and Vanishing Storm. UI source coverage reaches 266 strings; inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.60 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **256 UI strings**. Adds ten concise guide and move names, including Shadow Attack, Akira Guard, Super Dunk, Beat Spiral, Draciel Block, Wave Gate, Tiger Defense, and Driger Shadow. UI source coverage reaches 256 strings; inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.59 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **246 UI strings**. Adds ten concise guide and move names, including Blizz Rogue, Wing Dagger, Wing Typhoon, Hurricane Mixer, Cannon Bomber, and Super Escape. UI source coverage reaches 246 strings; inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.58 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **236 UI strings**. Adds ten short move names, including Catty and lightning attacks. UI source coverage reaches 236 strings; move-name inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.57 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **226 UI strings**. Adds ten more Beyblade move names from the guide tables. UI source coverage reaches 226 strings; move and guide inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.56 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **216 UI strings**. Adds ten short component and performance names to the guide. UI source coverage reaches 216 strings; guide inventory remains incomplete.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review remains deferred until the final UI version. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.55 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **206 UI strings**. Adds ten performance-tip and bearing names to the Beyblade guide. UI source coverage reaches 206 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.54 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **196 UI strings**. Adds ten blade-base and performance-tip names to the Beyblade guide. UI source coverage reaches 196 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.53 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **186 UI strings**. Adds ten attack-ring model names and abbreviations to the Beyblade guide. UI source coverage reaches 186 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.52 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **176 UI strings**. Adds ten additional attack-ring names to the Beyblade guide. UI source coverage reaches 176 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.51 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **166 UI strings**. Adds ten attack-ring model names to the Beyblade guide. UI source coverage reaches 166 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.50 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **156 UI strings**. Adds ten Beyblade launcher and attack-ring names to the guide. UI source coverage reaches 156 strings; guide inventory remains incomplete.

All new pointer-backed source strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. Visual review is deferred until the final UI version, as requested. No emulator run for this batch.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.49 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **146 UI strings**. Adds 18 compact model names, component labels and interface messages. UI source coverage reaches 146 strings; full interface and item-name inventory remain unfinished.

All new pointer-backed strings match the Japanese ROM and pass fixed display-capacity checks. Portable build and independent IPS verification passed once. A duplicate “no data” candidate was omitted because no direct pointer reference could be established. Visual review is deferred to the requested final UI verification. No emulator runs were performed for this batch.

Existing narrow font and battle fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.48 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **128 UI strings**. Adds launcher-selection prompts, part-category labels and special-move headings. UI source coverage reaches 128 strings; interface inventory remains incomplete.

All new source strings match the Japanese ROM, referenced pointers and fixed display capacities. Portable build and independent IPS verification passed once. Visual review is deferred to the requested final UI verification. No emulator runs were performed for this batch.

Existing narrow font and battle fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.47 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **117 UI strings**. Adds eight Beyblade and launcher selection prompts. UI source coverage reaches 117 strings; interface inventory remains incomplete.

All new source strings match the Japanese ROM, referenced pointers and fixed display capacities. Portable build and independent IPS verification passed once. Visual review is deferred to the requested final UI verification. No emulator runs were performed for this batch.

Existing narrow font and battle fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.46 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **109 UI strings**. Adds eight Beyblade-selection prompts and character lines. UI source coverage reaches 109 strings; interface inventory remains incomplete.

All new source strings match the Japanese ROM, referenced pointers and fixed display capacities. Portable build and independent IPS verification passed once. Visual review is deferred to the requested final UI verification. No emulator runs were repeated or performed for this batch.

Existing narrow font and battle fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.45 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **101 UI strings**. Adds 40 interface translations for part customization, communication status and parts trading, plus compact status labels. UI source coverage reaches 101 strings; full interface inventory remains incomplete.

The local portable build checked original bytes, pointers, display capacities, allocation and IPS application once. One 1200-frame local execution from the existing Beyblade Stats state was visually inspected; the displayed compact stat labels fit. The new customization and communication screens were not visually exercised because the local sample runner has no UI-resource mode and no matching saved states were available. No repeated runs were performed.

Existing narrow font and battle fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.44 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds the final 16 battle resources. All 837 text-bearing resource IDs in the battle table are translated across 1259 pages; 10 table slots are empty. This completes the battle table, not all text in the ROM.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (609, 610, 611) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 13 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.43 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for launch, Special Guard, Special S2 and Special 3 animation labels. Battle coverage reaches 821 of 837 text resources (98.1%) and 1237 pages, with 16 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (474, 475, 476) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 27 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.42 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for launch, Special Guard, Special S2 and Special 2/3 animation labels. Battle coverage reaches 791 of 837 text resources (94.5%) and 1198 pages, with 46 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (336, 337, 338) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 27 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.41 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for launch, Special Guard, Special 2/3, Special S1/S2 and evasion animation labels. Battle coverage reaches 761 of 837 text resources (90.9%) and 1159 pages, with 76 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (291, 292, 293) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 27 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.40 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for Special 2/3, launch, Special S1/S2 and evasion animation labels. Battle coverage reaches 731 of 837 text resources (87.3%) and 1123 pages, with 106 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (24, 25, 26) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 27 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.39 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for launch, Special Guard, Special S2 and Special 3 animation labels. Battle coverage reaches 701 of 837 text resources (83.8%) and 1078 pages, with 136 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (69, 70, 71) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box. These resources are animation-pattern labels, and natural gameplay use remains unconfirmed. The other 27 new resources were not visually sampled. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.38 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources covering Trygle attacks, Griffolyon moves, counterattacks, and Special Guard/Special 3 animation labels. Battle coverage reaches 671 of 837 text resources (80.2%) and 1039 pages, with 166 resources remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (403, 402, 404) were each emulated once with a single 1800-frame capture window. Because the final frame had returned to the tournament screen, captures from those same runs were inspected at frames 1200 (403 and 404) and 1500 (402); each showed a complete translated page fitting the dialogue box. For multi-page sequences, only the displayed page was visually checked; all remaining pages passed structural width and encoding checks, not screenshot review. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No emulator runs were repeated.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.37 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources: Rei's Driger attacks, Draciel's Wave Gate, Nobuo's Beat Spiral, Akira's special and counterattacks, and Seiichi's Shadow Attack. Battle coverage reaches 641 of 837 text resources (76.6%) and 958 pages, with 196 remaining.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (312, 179, 314) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box, though battle animation sprites overlap part of the text area in these fixtures. For multi-page sequences, only the page visible in the final capture was visually checked; all remaining pages passed structural width and encoding checks, not screenshot review. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.36 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources in resource IDs 63-68, 84-89, 108-113, 129-134, and 153-158. Battle coverage reaches 611 of 837 text resources (73.0%) and 871 pages, with 226 resources remaining.

The first QA backend attempt stopped during the automatic build because resource 87 exceeded the two-line page limit; no emulator samples ran on that attempt. After shortening the affected lines in resources 87 and 134, the second backend run built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (132, 87, 89) were each emulated once with a single 1800-frame capture window. The final capture from each run was visually inspected; the displayed text fit the dialogue box, though battle animation sprites overlap part of the text area in these fixtures. For multi-page sequences, only the page visible in the final capture was visually checked; all remaining pages passed structural width and encoding checks, not screenshot review. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No emulator runs were repeated.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.35 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 18, 19, 20, 21, 22, 23, 39, 40, 41, 42, 43, 44. Battle coverage reaches 581 resources and 774 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (674, 42, 43) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.34 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 633, 634, 635, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653. Battle coverage reaches 551 resources and 701 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (653, 628, 651) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.33 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 579, 580, 581, 582, 583, 584, 588, 589, 590, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 612, 613, 614, 615, 616, 617. Battle coverage reaches 521 resources and 650 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (582, 583, 584) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.32 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 537, 538, 539, 543, 544, 545, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 567, 568, 569, 570, 571, 572, 573, 574, 575. Battle coverage reaches 491 resources and 593 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (537, 538, 539) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.31 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 498, 499, 500, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 522, 523, 524, 525, 526, 527, 528, 529, 530, 534, 535, 536. Battle coverage reaches 461 resources and 539 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (517, 516, 518) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.30 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 faithful battle resources in resource IDs 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494. Battle coverage reaches 431 resources and 491 pages.

The local QA backend built the ROM and independently verified its IPS once. All translations passed source matching, page-count, command, encoding, width and allocation checks. The three largest new resources (494, 493, 492) were each emulated once with a single 1800-frame capture window. Captures from those same runs were visually inspected; only pages actually visible in the screenshots are claimed. The other 27 new resources were not visually sampled, and natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

Existing font, reaction-timer and highlighted-item crash fixes retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.29 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 attack, evasion and reaction resources featuring Griffolyon and Wolborg. Battle coverage reaches 401 resources and 434 pages.

The local backend built and independently verified the IPS once. All translations passed automatic source, page-count, command, encoding, width and allocation checks. The three largest new encoded resources (411, 413 and 412) were each emulated once. Completed-text captures at frame 480 were visually inspected; lines fit the text box. Similar wording is present in the Japanese originals. Defeat-animation sprites still overlap parts of the fixture display; natural context and timing remain unverified. The other 27 new resources were not visually sampled. No emulator runs were repeated.

Existing font, reaction-timer and highlighted-item crash fixes retained. New IDs: 408–422, 432–440, 453–455 and 459–461. Grat Shoot is a transliteration of the original move name, not a claim of verified official localized terminology. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.28 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources covering evasion, endurance and Trygle attacks. Battle coverage reaches 371 resources and 404 pages.

Initial construction rejected a line that wrapped to three lines in resources 387/390; the same wording was reflowed across two lines. Construction succeeded on the second attempt and independent IPS verification passed. No emulator ran during the failed build. The three largest new resources (342, 345 and 387) were each emulated once; completed-text captures at frame 480 were inspected and fit within the text box. Defeat-animation sprites overlap parts of the fixture display; natural context and timing remain unverified. Automatic checks cover all translations; the other 27 new resources were not visually sampled.

Engine fixes retained. New IDs: 342–350, 363–365, 369–377 and 387–395. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.27 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 attack, evasion, defense and reaction resources, including Akira lines and Shadow Attack sequences. Battle coverage reaches 341 resources and 374 pages.

The local backend built and independently verified the IPS once. All translations passed automatic source/page-count, command, encoding, width and allocation checks. The three largest new resources (335, 333 and 334) were each emulated once. Captures at frames 600 and 900 of the same runs were inspected. Both text pages were reached and fit the text box; defeat-animation sprites can still overlap the fixture display. The existing defeat-animation fixture is not a natural gameplay trigger or timing test; no complete campaign validation is claimed. The other 27 resources were not visually sampled. No emulator runs were repeated.

Existing engine fixes retained. New IDs: 279–287, 297–299, 303–308 and 324–335. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.26 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 resources including Max counterattacks and further attack, evasion and endurance lines. Battle coverage reaches 311 resources and 341 pages.

The local backend built and independently verified the IPS once. All translations passed source/page-count, command, encoding, width and allocation checks. The three largest new resources (224, 223 and 222) each ran once for 900 frames. Existing captures at frames 420, 600 and 900 were inspected. These four-page resources reached only the second text page within the capture window; the later pages were checked structurally but not visually. The fixture continues through defeat-animation sprites that can cover text. Natural triggers and full sequence timing remain unverified. No emulation was repeated.

The existing font and crash/timer fixes are retained. New IDs: 216–224, 234–245, 252–254, 258–260 and 273–275. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.25 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 35 battle resources for Rei and Max: attacks, defense, evasion and endurance (150–152, 162–173, 183–185, 189–197, 207–209 and 211–215). Battle coverage reaches 281 resources and 293 pages.

The local QA backend rebuilt the ROM and independently verified its IPS once. Automatic source checks cover all translations. The three largest new encoded resources (213, 215 and 190) were each emulated once. Captures at frames 420 and 480 of those same runs were inspected to see completed lines; no line exceeded the text-box width. Resources 213 and 215 intentionally contain identical source and translated dialogue. The existing fixture continues into its defeat animation, whose sprites can cover part of the text; these isolated tests do not verify natural character context or animation timing. The other 32 new resources were not visually sampled. No duplicate emulator runs were performed.

The narrow font, reaction-timer relocation and highlighted-item crash fix remain unchanged. Multi-page attack sequences and placeholder-labelled resources remain in the untranslated backlog. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.24 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 30 battle resources for Kai and Rei: attacks, evasion and reactions (93–95, 99–107, 117–125, 138–140 and 144–149). Battle coverage reaches 246 resources and 258 pages.

The local QA backend rebuilt the ROM and independently verified its IPS once. Automatic source checks cover every translation. The three largest new encoded resources (118, 119 and 94) were each emulated once. One completed-text capture per selected resource was visually inspected, with no clipping or overlap observed. The other 27 new resources were not visually sampled. Natural scene triggers remain unverified. Isolated fixtures use the existing battle context and do not establish the correct character portrait in natural gameplay. No duplicate emulator runs were performed.

The narrow font, reaction-timer relocation and highlighted-item crash fix remain unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.23 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 36 attack, evasion and endurance battle resources (27–38, 48–62 and 72–80), bringing battle coverage to 216 resources and 228 pages.

The local QA backend rebuilt the ROM and independently verified its IPS once. Automatic source checks cover all translations. The three largest new encoded resources (78, 33 and 74) were each emulated once. One completed-text capture per resource was inspected, with no clipping or overlap observed. The other 33 new resources were not visually sampled; natural gameplay triggers remain unverified. No duplicate emulator runs were performed.

The narrow font, reaction-timer relocation and highlighted-item crash fix remain unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.22 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 45 defeat and end-of-battle reaction resources (786–827 and 831–833), bringing battle coverage to 180 resources and 192 pages.

The local QA backend rebuilt the ROM and independently verified its IPS once. Source checks cover all translations. The three largest new encoded resources (795, 831 and 820) were each emulated once; one completed-text capture per resource was inspected, with no clipping or overlap observed. The other 42 new resources were not visually sampled. Natural gameplay triggers remain unverified. No duplicate emulation runs were performed.

The existing narrow font, reaction-timer relocation and highlighted-item crash fix are retained. Future retries are limited to three attempts per case, and require a failure or relevant correction. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.21 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds 45 combat reaction resources (738–779 and 783–785), bringing battle coverage to 135 resources and 147 pages.

The local browser app executed the actual /run workflow with the new-resource filter and selected the three largest encoded resources: 738, 763 and 739. Automatic source checks, portable reconstruction and independent IPS verification passed. One completed-text capture per selected resource was visually inspected: both lines fit without clipping or overlap. The remaining 42 new resources were not visually sampled; natural gameplay triggers were not verified. The app report retains its pending human-review status. The default visual sample is now three; automatic checks still cover every translation.

The reaction-timer relocation and highlighted-item crash fix from versions 0.19 and 0.20 are retained. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.20 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Fixes the post-battle parts-reward crash when rendering highlighted item names. Translation counts and the upper-right reaction-timer layout remain unchanged.

The user's native mGBA PNG save state was preserved and its gbAs chunk decompressed into a private test state. Loading it with v0.18 reproduced the stall/invalid execution while displaying the received part category. With v0.20, the same state advanced through the highlighted item name, the translated reward continuation, and the following message in one targeted 240-frame replay. Screenshots were inspected at the item and continuation stages. A byte-difference audit restricts changes from v0.19 to the HH call site and its new trampoline. Portable reconstruction and independent IPS verification passed. No additional whole-battle or full-game retest is claimed.

The HH branch originally targeted FCAC, inside the font-selector BL inserted at FCAA. A dedicated trampoline at 0x400100 now preserves HH's narrow-font arguments and resumes at FCAE, past the complete selector instruction. No reward data or combat rules change. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.19 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Moves the five-cell battle reaction timer from above the dialogue to the upper-right arena, immediately below the health/energy HUD. This release changes layout only; translation counts remain unchanged.

Version 0.18 and 0.19 were replayed from the same pre-attack battle state at six matching frame counts (600, 720, 840, 960, 1100, 2040). The 20 timer tile entries matched at the new location, allowing only the intended blue-to-transparent clearing substitution. The clearing tile was confirmed transparent in VRAM. Screenshots covering the active timer, partial countdown, cleared arena, and a second attack were visually inspected. A byte-difference audit restricts changes from v0.18 to three timer destination literals, two clearing call sites, and two small clearing helpers. Independent IPS application and portable reconstruction passed. This does not establish full-game or hardware coverage.

The timer's three BG1 destination literals move it from tile rows 15-16 to rows 5-6, preserving its horizontal position. Individual-cell and whole-timer clearing now use the existing transparent tile rather than the dialogue's blue background. Countdown logic, duration, input handling, and block colors are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.18 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **61 UI strings**. Adds a separate translation source for 90 group-2 battle resources, including the two phrases supplied in the user's screenshots, recurrent selection and defeat remarks, 12 DJ commentary resources, and 18 early attack/launch resources. UI coverage increases to 61 strings, including battle commands, selected move labels, and roster text names. These battle counts are separate from the unchanged 542 story/result speeches.

All 90 resources pass original-page matching, page-count, encoding, two-line/24-cell limit, dynamic-name sequence, allocation, and pointer checks. Independent IPS application and portable reconstruction passed. Actual arena rendering was inspected from a pre-launch state: a launch-miss DJ comment and ending comment occurred naturally. Resources 678 and 843, matching the user's screenshots, were additionally injected into the active battle renderer in test-only emulator RAM and inspected through their English pages. This is not natural-trigger coverage for those two resources. Roster text names translate in dynamically rendered commentary; previously cached names and separate graphic labels can remain Japanese. The battle command labels are inserted with 8-cell capacities and move labels with 12-cell capacities, but their natural menu layouts are not yet visually verified. Full battles, remaining combat text, hardware, and save/load remain unverified.

The battle interpreter now has a 60-byte temporary line buffer and selects the existing narrow font for relocated English streams only. Battle animations, portrait parameters, waits, page breaks, and end metadata remain intact; the optional Japanese name honorific is omitted in English. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.17 — experimental, local draft

The editable sources contain **542 speeches in 264 scenes (353–616)** and **35 UI strings**. Adds 33 speeches across 12 resources: parts and shooter reward continuations and three variants of Kaoru's defeat and Masamune's departure. The builder now preserves headerless continuation resources using a null speaker instead of adding a portrait command.

All added resources passed automatic command, encoding, name-count, speaker-sequence, line-width, and ending checks. All 12 were visually inspected in isolated substitution fixtures because this batch introduces headerless resources and more dynamic names. Headerless fixtures first establish Kyouju's portrait using resource 604, then run the unchanged translated continuation bytes. This validates inherited portrait display in that fixture, not the natural reward caller. Default Daichi name rendering was checked; entered names, natural final-event triggers, and full-game behavior remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.16 — experimental, local draft

The editable sources contain **509 speeches in 252 scenes (353–604)** and **35 UI strings**. Adds 35 battle-result and reward speeches, including Kyouju's advice, level-up announcements, and parts rewards. The batch stops before resource 605, which lacks the leading speaker header expected by the current builder and requires separate engine analysis.

All 35 added scenes passed automatic speaker-sequence, command, runtime-name count, encoding, line-width, and ending checks. The six largest encoded resources (602, 597, 595, 599, 598, 596), plus runtime-name resource 601, were advanced and visually inspected in isolated resource-substitution copies. Dynamic names were checked with the default Daichi name. The other 28 resources were not individually emulator-tested. Natural gameplay triggers and custom entered names remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.15 — experimental, local draft

The editable sources contain **474 speeches in 217 scenes (353–569)** and **35 UI strings**. Adds 40 battle-result speeches for Kaoru, Daichi, Takao, Kai, Rei, and Max, mainly reactions to defeat and rematch challenges. Visual sampling selects the six largest encoded resources in this batch, resolving equal lengths by scene ID.

All 40 added scenes passed automatic speaker-sequence, supported-command, name-command count, encoding, line-width, and scene-ending checks. The six longest encoded resources (531, 538, 540, 553, 555, 558) were advanced and visually inspected in isolated resource-substitution copies for pagination, text fit, portraits, and termination. The remaining 34 resources were not individually emulator-tested. Natural battle-result triggers and full-game coverage remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.14 — experimental, local draft

The editable sources contain **434 speeches in 177 scenes (353–529)** and **35 UI strings**. Adds 40 post-battle speeches, principally for the White Tiger Clan and Kaoru. This batch adopts visual sampling for established dialogue formats instead of emulating every new short resource.

All 40 added scenes passed automatic speaker-sequence, command, name-command count, encoding, line-width, and scene-ending validation. Six selected resources (491, 498, 504, 514, 521, 529) were advanced and visually inspected in isolated resource-substitution copies, prioritizing longer lines. The other 34 added resources were not individually inspected in the emulator. Natural post-battle triggers and full-game coverage remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.13 — experimental, local draft

The editable sources contain **394 speeches in 137 scenes (353–489)** and **35 UI strings**. Adds 20 post-battle speeches for Max and other rivals, including opponent-specific remarks, duplicate-character reactions, and references to Trygle and Bit Beasts. Repeated Japanese lines retain identical English wording.

All twenty added resources were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for text layout, pagination, speaker portraits, and termination. Their natural post-battle triggers remain unverified; these checks do not establish full-game coverage.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.12 — experimental, local draft

The editable sources contain **374 speeches in 117 scenes (353–469)** and **35 UI strings**. Adds 20 post-battle speeches for Kai, Rei, and Max, including opponent-specific remarks and duplicate-character reactions. Repeated Japanese lines retain identical English wording.

All twenty added resources were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for text layout, pagination, speaker portraits, and termination. Their natural post-battle triggers remain unverified; these checks do not establish full-game coverage.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.11 — experimental, local draft

The editable sources contain **354 speeches in 97 scenes (353–449)** and **35 UI strings**. Adds 28 speeches covering another tournament-introduction variant and 17 post-battle lines for Daichi, Takao, and Kai. Original character names and Beyblade names remain consistent.

All twenty added resources were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for text layout, pagination, speaker changes, and termination. Their natural tournament and post-battle triggers remain unverified; these checks do not establish full-game coverage.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.10 — experimental, local draft

The editable sources contain **326 speeches in 77 scenes (353–429)** and **35 UI strings**. Adds 30 speeches covering alternate park introductions, including Daichi meeting Seiichi and Takao discussing tournament qualification. Identical Japanese resources share consistent translations, while the omitted boast in scene 427 remains omitted.

All eight added scenes were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for text layout, pagination, speaker changes, and scene termination. Natural route triggers and full-game behavior remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.9 — experimental, local draft

The editable sources contain **296 speeches in 69 scenes (353–421)** and **35 UI strings**. Adds 28 speeches covering the remaining Takao and custom-player championship award and challenge variants. All six runtime-name occurrences in the added scenes are preserved.

All eight added scenes were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for layout, pagination, speaker changes, runtime-name rendering with the default Daichi name, and scene termination. Custom entered names and natural later-stage triggers remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.8 — experimental, local draft

The editable sources contain **268 speeches in 61 scenes (353–413)** and **35 UI strings**. Adds 46 speeches covering final-league preparations, championship announcements and awards for Daichi and Takao, and the arrival of Chizan Masamune and Kaoru.

All thirteen added scenes were advanced to completion in isolated resource-substitution copies. Timed screenshots were inspected for text layout, pagination, speaker changes, and scene termination. Natural later-stage triggers and full-game behavior remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.7 — experimental, local draft

The editable sources contain **222 speeches in 48 scenes (353–400)** and **35 UI strings**. Adds 40 speeches covering the representatives' selection, the Asian qualifier results, and Rei's second-chance round. The runtime-name command in scene 395 remains intact.

All ten added scenes were advanced in isolated resource-substitution copies. Timed screenshots were inspected for text layout, speaker changes, name substitution, and scene termination. Natural later-stage triggers and full-game behavior remain unverified.

The font and memory layout are unchanged. The portable build reproduced the development ROM and IPS byte-for-byte; independent IPS verification passed. The original ROM remains unchanged. No full-game, hardware, multiplayer, complete-battle, or save/load validation is claimed.

## Historical snapshot: 0.6 — experimental, local draft

The editable script contains **182 speeches across 38 scenes, 353–390 inclusive**, and **35 UI strings**. This batch adds 40 speeches in eight scenes: the additional Kaoru encounter, regional qualifying results, Kai's appearance, and Kyouju's invitation to join the team as mechanic.

All eight added scenes were advanced in isolated resource-substitution copies using mGBA. Timed screenshots were inspected for text layout, speaker changes, and scene termination. Their natural gameplay triggers have not yet been exercised. No full-game, hardware, multiplayer, save/load, or complete-battle validation is claimed.

The font and memory layout are unchanged from version 0.5. The portable build reproduced the development ROM and IPS byte-for-byte, and independent application of the 163-record patch reconstructed the built ROM exactly. The original ROM remains unchanged.

Project release naming now lives in `project.json`. Run `python tools/status.py` to derive current progress counts directly from editable sources without a ROM. This avoids treating copied README numbers as the authoritative inventory.

## Historical snapshot: version 0.5

The editable script contains **142 speeches across all 30 scenes from 353 through 382**, plus **35 UI strings**. The nine added scenes cover tournament transitions, Max and Takao's reunion, Kai's challenge, and both versions of the Kaoru encounter.

All nine added scenes were advanced in separate resource-substitution validation copies. English pages, speaker changes, scene termination, and the name command in scene 380 were inspected. These are isolated playback checks; the natural later-stage triggers remain unverified.

The previous 32 KiB dialogue allocation was replaced with a larger reserved pool so that the script can continue growing. The font hook is now at file offset `0x400000`, translated dialogue begins at `0x410000`, and UI strings begin at `0x7F0000`. Collision and capacity checks remain active. The ROM is still 8 MiB. After this change, a long Kaoru scene and the name-command scene were rerun; all 65 captured screenshots matched their earlier renderings byte-for-byte. The opening dialogue and shooter menu were also checked with the new allocation.

Full-game progression, complete battles, multiplayer, hardware, saving, loading, and compatibility with previous-version save states remain unverified. Start a fresh game for cross-version testing instead of relying on a mid-dialogue state from an older patch.

## Historical snapshot: version 0.4

The script now contains **94 speeches in 21 scenes, 353–373 inclusive**, and **35 UI strings**. This fills the previously skipped name-command scenes 365 and 371 and adds Daichi's encounters with Mao, Rei, and Max (367, 368, 373).

The source placeholder `{N1}` preserves the original runtime name command. It appears on its own line, and the build checks that the command count matches the original scene. Both default Daichi and Takao names were inspected in isolated tests; names still render in Japanese. Other name commands and longer or customized names remain unverified.

Validation in this batch:

- Scenes 367, 368, and 373 were advanced through all pages in isolated resource-substitution copies, with speaker changes and termination inspected.
- Scenes 365 and 371 were checked with Daichi; scene 365 was also checked with Takao in a separate substitution copy.
- Takao's normal introductory progression was run again and reached the first battle. This is a regression check, not evidence that the later scenes' natural triggers have been tested.
- The portable build reproduced the development ROM and IPS. Independent application of the 145-record patch reconstructed the ROM byte-for-byte.

The current patched ROM SHA-256 is `e52d88c6fb4b3157b179535d83b6489980ec608289df6025ac28b0c8114aa5e2`. Source ROM requirements are unchanged. No full-game, multiplayer, hardware, or save/load round-trip test is claimed.

Next work: map and translate subsequent scenes, expand the resource-based inventory, and continue visual and progression tests. Many battle instructions, image-based menu labels, dynamic part names, and later scenes remain Japanese. The preliminary extracted-candidate total remains unsuitable for a completion percentage.

## Historical snapshot: version 0.3

The editable script contains **53 translated speeches in 16 scenes**: 353–364, 366, 369, 370, and 372. There are **35 translated UI strings**. Japanese names are retained, and translated dialogue uses the built-in narrow font with extra pages.

The script is intentionally incomplete. Gaps in the scene list remain Japanese, including scene 365, which contains a runtime name command that the builder does not yet support.

## What has been tested

| Area | Method | Result and limit |
| --- | --- | --- |
| Daichi opening, scenes 353–360 | Normal Stage 1 progression in version 0.2 | Reached the first NEXT BATTLE screen; no full battle completed in that run |
| Takao opening, scenes 361–364 | Normal character selection and progression in version 0.2 | Reached the first battle; the following name-variable speech remains Japanese |
| New scenes 366, 369, 370, 372 | Separate validation copies temporarily point the first scene entry at each new scene | English pages, portraits, and scene termination inspected; natural stage-2 triggers not tested |
| Guide categories | Actual Attack Ring, Weight Disk, and Blade Base tabs | Category labels inspected |
| Shooter selection | Actual screen and confirmation | English labels displayed and choice accepted |
| Status | Actual character attributes and Beyblade Stats screen | Changed labels inspected; other pages still need coverage |
| Build reproducibility | Clean portable scripts given an external original ROM | Result matched the development ROM and IPS byte-for-byte |
| IPS verification | Independent patch application | Reconstructed the built ROM byte-for-byte |

Tests used the mGBA libretro core. Emulated button sequences and screenshots were used for inspection. Some captures show text during its normal letter-by-letter reveal. No full-game, multiplayer, hardware, or save/load round-trip validation is claimed.

## Still pending

- Map runtime name substitutions and other unsupported commands.
- Replace heuristic extraction with a resource-based inventory and verified scene boundaries.
- Translate the remaining scenes and review the English against Japanese context.
- Map dynamic part names and image-based menu labels.
- Improve page breaks at sentence boundaries when practical.
- Test all modified UI fields, battle flows, saving, loading, and natural later-stage progression.
- Decide project licensing and publish the reviewed repository draft.

The 1,251 extracted candidate speeches do not establish a full-game total. Do not calculate a public completion percentage from that preliminary number.

## Changes by version

- **0.1:** 12 speeches; initial narrow-font prototype and UI batch.
- **0.2:** 42 speeches, 35 UI strings, natural introductory progression checks.
- **0.3:** 53 speeches, 35 UI strings, four isolated later-scene playback checks, a portable build and patcher, character table, contribution guide, and technical documentation.
- **0.4:** 94 speeches, 35 UI strings, three more rival encounters, support and isolated checks for `{N1}`, and another natural Takao opening regression run.
- **0.5:** 142 speeches, 35 UI strings, nine more tournament and rival scenes, and expanded translation-data allocation with rendering checks.

- **0.6:** 182 speeches, 35 UI strings, eight more scene playback checks, and source-derived progress reporting.

- **0.7:** 222 speeches, 35 UI strings; 10 added scenes inspected in isolation.

- **0.8:** 268 speeches, 35 UI strings; 13 added scenes inspected in isolation.

- **0.9:** 296 speeches, 35 UI strings; 8 added scenes inspected in isolation.

- **0.10:** 326 speeches, 35 UI strings; 8 added scenes inspected in isolation.

- **0.11:** 354 speeches, 35 UI strings; 20 added scenes inspected in isolation.

- **0.12:** 374 speeches, 35 UI strings; 20 added scenes inspected in isolation.

- **0.13:** 394 speeches, 35 UI strings; 20 added scenes inspected in isolation.

- **0.14:** 434 speeches, 35 UI strings; 6 added scenes inspected in isolation.

- **0.15:** 474 speeches, 35 UI strings; 6 added scenes inspected in isolation.

- **0.16:** 509 speeches, 35 UI strings; 7 added scenes inspected in isolation.

- **0.17:** 542 speeches, 35 UI strings; 12 added scenes inspected in isolation.

- **0.18:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.19:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.20:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.21:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.22:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.23:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.24:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.25:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.26:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.27:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.28:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.29:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.30:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.31:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.32:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.33:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.34:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.35:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.36:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.37:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.38:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.39:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.40:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.41:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.42:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.43:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.44:** 542 speeches, 61 UI strings; 0 added scenes inspected in isolation.

- **0.45:** 542 speeches, 101 UI strings; 0 added scenes inspected in isolation.

- **0.46:** 542 speeches, 109 UI strings; 0 added scenes inspected in isolation.

- **0.47:** 542 speeches, 117 UI strings; 0 added scenes inspected in isolation.

- **0.48:** 542 speeches, 128 UI strings; 0 added scenes inspected in isolation.

- **0.49:** 542 speeches, 146 UI strings; 0 added scenes inspected in isolation.

- **0.50:** 542 speeches, 156 UI strings; 0 added scenes inspected in isolation.

- **0.51:** 542 speeches, 166 UI strings; 0 added scenes inspected in isolation.

- **0.52:** 542 speeches, 176 UI strings; 0 added scenes inspected in isolation.

- **0.53:** 542 speeches, 186 UI strings; 0 added scenes inspected in isolation.

- **0.54:** 542 speeches, 196 UI strings; 0 added scenes inspected in isolation.

- **0.55:** 542 speeches, 206 UI strings; 0 added scenes inspected in isolation.

- **0.56:** 542 speeches, 216 UI strings; 0 added scenes inspected in isolation.

- **0.57:** 542 speeches, 226 UI strings; 0 added scenes inspected in isolation.

- **0.58:** 542 speeches, 236 UI strings; 0 added scenes inspected in isolation.

- **0.59:** 542 speeches, 246 UI strings; 0 added scenes inspected in isolation.

- **0.60:** 542 speeches, 256 UI strings; 0 added scenes inspected in isolation.

- **0.61:** 542 speeches, 266 UI strings; 0 added scenes inspected in isolation.

- **0.62:** 542 speeches, 272 UI strings; 0 added scenes inspected in isolation.

- **0.63:** 542 speeches, 282 UI strings; 0 added scenes inspected in isolation.

- **0.64:** 542 speeches, 292 UI strings; 0 added scenes inspected in isolation.

- **0.65:** 542 speeches, 302 UI strings; 0 added scenes inspected in isolation.

- **0.66:** 542 speeches, 312 UI strings; 0 added scenes inspected in isolation.

- **0.67:** 542 speeches, 322 UI strings; 0 added scenes inspected in isolation.

- **0.68:** 542 speeches, 332 UI strings; 0 added scenes inspected in isolation.

- **0.69:** 542 speeches, 342 UI strings; 0 added scenes inspected in isolation.

- **0.70:** 542 speeches, 352 UI strings; 0 added scenes inspected in isolation.

- **0.71:** 542 speeches, 362 UI strings; 0 added scenes inspected in isolation.

- **0.72:** 542 speeches, 372 UI strings; 0 added scenes inspected in isolation.

- **0.73:** 542 speeches, 382 UI strings; 0 added scenes inspected in isolation.

- **0.74:** 542 speeches, 392 UI strings; 0 added scenes inspected in isolation.

- **0.75:** 542 speeches, 395 UI strings; 0 added scenes inspected in isolation.

- **0.76:** 542 speeches, 405 UI strings; 0 added scenes inspected in isolation.

- **0.77:** 542 speeches, 415 UI strings; 0 added scenes inspected in isolation.

- **0.78:** 542 speeches, 425 UI strings; 0 added scenes inspected in isolation.

- **0.79:** 542 speeches, 435 UI strings; 0 added scenes inspected in isolation.

- **0.80:** 542 speeches, 445 UI strings; 0 added scenes inspected in isolation.

- **0.81:** 542 speeches, 454 UI strings; 0 added scenes inspected in isolation.

- **0.82:** 542 speeches, 463 UI strings; 0 added scenes inspected in isolation.

- **0.83:** 542 speeches, 473 UI strings; 0 added scenes inspected in isolation.

- **0.84:** 542 speeches, 483 UI strings; 0 added scenes inspected in isolation.

- **0.85:** 542 speeches, 493 UI strings; 0 added scenes inspected in isolation.

- **0.86:** 542 speeches, 503 UI strings; 0 added scenes inspected in isolation.

- **0.87:** 542 speeches, 513 UI strings; 0 added scenes inspected in isolation.

- **0.88:** 542 speeches, 523 UI strings; 0 added scenes inspected in isolation.

- **0.89:** 542 speeches, 533 UI strings; 0 added scenes inspected in isolation.

- **0.90:** 542 speeches, 543 UI strings; 0 added scenes inspected in isolation.

- **0.91:** 542 speeches, 553 UI strings; 0 added scenes inspected in isolation.

- **0.92:** 542 speeches, 553 UI strings; 0 added scenes inspected in isolation.

- **0.93:** 542 speeches, 557 UI strings; 0 added scenes inspected in isolation.

- **0.94:** 542 speeches, 562 UI strings; 0 added scenes inspected in isolation.

- **0.95:** 542 speeches, 567 UI strings; 0 added scenes inspected in isolation.

- **0.96:** 542 speeches, 572 UI strings; 0 added scenes inspected in isolation.

- **0.97:** 542 speeches, 577 UI strings; 0 added scenes inspected in isolation.

- **0.98:** 542 speeches, 582 UI strings; 0 added scenes inspected in isolation.

- **0.99:** 542 speeches, 590 UI strings; 0 added scenes inspected in isolation.

- **1.00:** 548 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.01:** 554 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.02:** 560 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.03:** 566 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.04:** 572 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.05:** 577 speeches, 590 UI strings; 3 added scenes inspected in isolation.

- **1.06:** 577 speeches, 598 UI strings; 0 added scenes inspected in isolation.

- **1.07:** 577 speeches, 606 UI strings; 0 added scenes inspected in isolation.

- **1.08:** 577 speeches, 610 UI strings; 0 added scenes inspected in isolation.

- **1.09:** 581 speeches, 610 UI strings; 1 added scenes inspected in isolation.

- **1.10:** 583 speeches, 610 UI strings; 1 added scenes inspected in isolation.

- **1.11:** 585 speeches, 610 UI strings; 1 added scenes inspected in isolation.

- **1.12:** 585 speeches, 620 UI strings; 0 added scenes inspected in isolation.

- **1.13:** 585 speeches, 628 UI strings; 0 added scenes inspected in isolation.

- **1.14:** 585 speeches, 644 UI strings; 0 added scenes inspected in isolation.

- **1.15:** 585 speeches, 656 UI strings; 0 added scenes inspected in isolation.

- **1.16:** 585 speeches, 662 UI strings; 0 added scenes inspected in isolation.

- **1.17:** 585 speeches, 668 UI strings; 0 added scenes inspected in isolation.

- **1.18:** 585 speeches, 674 UI strings; 0 added scenes inspected in isolation.

- **1.19:** 585 speeches, 680 UI strings; 0 added scenes inspected in isolation.

- **1.20:** 585 speeches, 686 UI strings; 0 added scenes inspected in isolation.

- **1.21:** 585 speeches, 692 UI strings; 0 added scenes inspected in isolation.

- **1.22:** 585 speeches, 698 UI strings; 0 added scenes inspected in isolation.

- **1.23:** 585 speeches, 704 UI strings; 0 added scenes inspected in isolation.

- **1.24:** 585 speeches, 710 UI strings; 0 added scenes inspected in isolation.

- **1.25:** 585 speeches, 716 UI strings; 0 added scenes inspected in isolation.

- **1.26:** 585 speeches, 722 UI strings; 0 added scenes inspected in isolation.

- **1.27:** 585 speeches, 728 UI strings; 0 added scenes inspected in isolation.

- **1.28:** 585 speeches, 734 UI strings; 0 added scenes inspected in isolation.

- **1.29:** 585 speeches, 740 UI strings; 0 added scenes inspected in isolation.

- **1.30:** 585 speeches, 746 UI strings; 0 added scenes inspected in isolation.

- **1.31:** 585 speeches, 751 UI strings; 0 added scenes inspected in isolation.

- **1.32:** 585 speeches, 755 UI strings; 0 added scenes inspected in isolation.

- **1.33:** 585 speeches, 759 UI strings; 0 added scenes inspected in isolation.

- **1.34:** 585 speeches, 763 UI strings; 0 added scenes inspected in isolation.

- **1.35:** 585 speeches, 768 UI strings; 0 added scenes inspected in isolation.

- **1.36:** 585 speeches, 773 UI strings; 0 added scenes inspected in isolation.

- **1.37:** 585 speeches, 778 UI strings; 0 added scenes inspected in isolation.

- **1.38:** 585 speeches, 782 UI strings; 0 added scenes inspected in isolation.

- **1.39:** 585 speeches, 786 UI strings; 0 added scenes inspected in isolation.

- **1.40:** 585 speeches, 791 UI strings; 0 added scenes inspected in isolation.

- **1.41:** 585 speeches, 796 UI strings; 0 added scenes inspected in isolation.

- **1.42:** 585 speeches, 801 UI strings; 0 added scenes inspected in isolation.

- **1.43:** 585 speeches, 806 UI strings; 0 added scenes inspected in isolation.

- **1.44:** 585 speeches, 811 UI strings; 0 added scenes inspected in isolation.

- **1.45:** 585 speeches, 816 UI strings; 0 added scenes inspected in isolation.

- **1.46:** 585 speeches, 816 UI strings; 0 added scenes inspected in isolation.

- **1.47:** 585 speeches, 816 UI strings; 0 added scenes inspected in isolation.

- **1.48:** 585 speeches, 816 UI strings; 0 added scenes inspected in isolation.
