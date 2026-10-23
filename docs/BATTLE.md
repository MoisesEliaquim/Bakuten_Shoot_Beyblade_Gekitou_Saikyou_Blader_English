# Battle text — current status v1.48

Battle text uses resource group 2, whose relative-pointer base is file offset `0x32AACC`. It is separate from group 1, used by the existing story/result translation.

| User screenshot text | Group-2 resource | Original file offset |
| --- | ---: | --- |
| `きあいバッチリ / ぜんかいでいこうぜっ！` | 678 | `0x33739C` |
| `N1∝！？ / そろそろ本気をださないと` and its following page | 843 | `0x33900C` |

A fonte editável `translations/battle-en.json` cobre 837 recursos com texto da tabela do grupo 2, total de 1.259 páginas. A varredura dos índices 0–846 encontrou os 837 recursos com texto traduzidos; dez entradas não têm texto. O recurso 846 contém apenas espaço e comandos de controle. Isso cobre o conteúdo textual enumerado nessa tabela, mas não confirma todos os acionamentos naturais ou todos os eventos do jogo.

Na QA v1.48, o build e a verificação independente do IPS passaram. As fixtures dos recursos 42, 43 e 674 foram revisadas visualmente; uma página útil apareceu por recurso e o restante foi validado estruturalmente. A substituição de RAM usada pela QA não prova acionamento natural.

`tools/battle_patch.py`, invoked by `build_ui.py`, relocates these streams into the reserved pool beginning at `0x500000`. It checks the original pages and dynamic-name sequence and retains `FF` parameters, `WF` wait values, `PP`, and the complete `EE` tail, including metadata. `KK` line wrapping can change. The optional `∝` marker adds a Japanese honorific after a name; the English stream omits that marker and retains the runtime `N1`/`N2` command.

The battle interpreter at `0x0801E8DC` uses a separate temporary line buffer and draw call. Its buffer grows from 28 to 60 bytes by expanding the stack frame at `0x1E8E6` and its matching cleanup at `0x1EB0A`. A font-selection hook at `0x400040`, called from `0x1EB02`, chooses narrow characters only for relocated streams in `0x08400000`–`0x087FFFFF`. Untranslated Japanese streams keep the original font mode. English pages are limited to two 24-cell lines; dynamic names reserve eight cells each.

Version 0.18 adds `Special`, `Evade`, `Guard`, and `Counter` at original string offsets `0x465E4`, `0x465F0`, `0x465F8`, and `0x46600`, as well as selected move labels and roster text names. The explicit display capacities in the UI source apply only to these additions; their natural command-menu layout still requires visual verification. Some HUD/selection names may use cached data or graphics rather than the translated text pointers.

Actual arena rendering was checked from a pre-launch state. Launch-miss and ending DJ comments occurred naturally. The screenshot resources 678 and 843 were also selected by a test-only RAM override of the active battle stream, not by changing the shipped gameplay logic. Resource 843's second page was checked after its wait/page transition. These checks do not establish natural triggering for every translated line or complete-battle coverage.

The arena's graphical player/enemy labels, graphics in selection screens, untranslated attack scripts, and complete natural menu/event coverage remain outstanding. Version 0.18 does not constitute a complete battle-interface translation.
