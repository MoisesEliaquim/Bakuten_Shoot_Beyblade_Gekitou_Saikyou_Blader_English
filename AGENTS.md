# Continuação da tradução de Beyblade

Leia este guia antes de editar ou construir o patch. Os metadados mais recentes em `patches/release-v150.json` e as fontes editáveis prevalecem se este resumo ficar desatualizado.

## Projeto e estado confirmado

- O jogo é **Bakuten Shoot Beyblade: Gekitou! Saikyou Blader**, de Game Boy Advance, versão japonesa identificada pelo código **AHEJ**.
- O objetivo é traduzir o jogo do japonês para o inglês com fidelidade ao original. O projeto segue experimental; não declarar a tradução completa nem o jogo integralmente testado.
- Estado v1.50 experimental: **587 falas em 308 cenas**, **816 strings de UI**, **28 recursos estruturados com 62 strings**, e **837 recursos de batalha em 1.259 páginas**.
- A revisão visual confirmou que o título `Beyblade` está centralizado no campo do catálogo. A captura de Custom A mostra ainda em japonês os sete rótulos de status (Speed, Attack, Guard, Balance, Weight, Search e Active). Os rótulos gráficos do menu inicial e do hub também permanecem em japonês. Localizar a origem gráfica/ponteiros desses textos segue pendente.
- O build portátil e a verificação independente do IPS v1.50 passaram, com 2.289 registros. A cena 312 passou as verificações de comandos, falantes, codificação, largura e alocação. A captura de QA permaneceu na cena japonesa 353 já carregada pelo estado salvo; nenhuma das frases novas foi confirmada visualmente. Isso não significa que o jogo completo foi testado.
- Há fatos ainda não confirmados: a origem e os ponteiros dos rótulos gráficos; a cobertura visual total do jogo; e a semântica completa dos comandos de texto não mapeados na documentação técnica.
- Auditoria estática: a cena 311 só contém espaço e terminador; a cena 312 agora tem rascunho em inglês (“Gah...”, “N-no way...” e “This is a test.”), mas a exibição e o acionamento natural não foram confirmados. O grupo 2 tem 837 recursos com texto traduzidos em 1.259 páginas; dez entradas da tabela não têm texto. Fixtures dos recursos 42, 43 e 674 foram revisadas, sem comprovar acionamento natural.

## Preferências de tradução e revisão

- Em falas, escrever **Eight** por extenso; em nomes de peças, usar o numeral **8**.
- Manter nomes consistentes (por exemplo, Kai, Max, Masamune, Kaoru e Kiyoshi) e preservar nomes editoriais conforme a fonte.
- Preservar a fonte estreita preferida. Ajustar o texto para caber sem perder sentido; páginas extras só podem usar comandos que o jogo suporte.
- Em cada lote, verificar automaticamente todas as traduções e revisar visualmente três amostras de maior risco (marcadores raros, texto compacto ou longo, caracteres especiais). Uma execução por amostra; repetir apenas após falha ou correção relevante, no máximo três tentativas por caso.
- Conversar e documentar em português; os textos do jogo permanecem em inglês. Não usar estilo “caveman”.

## Arquivos para continuar e publicar

Na pasta `beyblade-english/` está o rascunho publicável. Arquivos essenciais:

- `patches/Beyblade-AHEJ-English-v150-EXPERIMENTAL.ips` — patch atual para distribuição.
- `translations/dialogue-en.json`, `translations/menus-en.json`, `translations/battle-en.json` e `translations/structured-menus-en.json` — fontes editáveis de falas, UI, batalha e menus/eventos estruturados.
- `tables/beyblade-ahej.tbl` — tabela de caracteres para inspeção.
- `project.json` — nome-base dos artefatos gerados.
- `tools/build.py`, `build_dialogue.py`, `build_ui.py`, `battle_patch.py`, `verify_patch.py` e `apply_patch.py` — construção, validação e aplicação do IPS. `extract_dialogue.py` auxilia a extração.
- `README.md`, `README.pt-BR.md`, `CONTRIBUTING.md` e `docs/` — uso e colaboração. Priorize `docs/FORMAT.md`, `BATTLE.md`, `VALIDATION.md`, `PROGRESS.md`, `CONTINUATIONS.md` e `PUBLISHING.md` para detalhes técnicos, limites conhecidos e publicação.
- `patches/release-v150.json` — metadados e estado de validação do patch atual.

Inclua no GitHub as fontes, ferramentas, documentação e **somente o IPS atual**. Não inclua ROMs (`*.gba`), saves (`*.sav`), estados do emulador (`*.state`, `*.ss0`, `*.ss1`), núcleo/bibliotecas ou executáveis do mGBA (`*.dll`, `*.exe`), caches (`__pycache__`, `*.pyc`), logs, capturas e saídas de build. Não envie referências privadas, `beyblade-translation/`, `beyblade-english/private/` ou versões históricas do IPS. Em particular, `beyblade-english/build/` é saída local com mais de 2 GB e deve ficar fora do repositório. O `.gitignore` já cobre várias dessas classes, mas revise os arquivos selecionados antes de publicar.

## Fluxo de build, verificação e aplicação

1. Obtenha do usuário a ROM japonesa original compatível. Ela precisa ter SHA-256 `58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c`. A ROM não é distribuída pelo projeto, não deve ser adicionada ao GitHub e nunca deve ser sobrescrita.
2. Com Python 3.10 ou mais recente, entre em `beyblade-english/` e rode `python tools/build.py --rom "CAMINHO/DA/ROM-ORIGINAL.gba"`. O script constrói em `build/` (ou use `--output-dir`) e executa a verificação independente do IPS. A saída é local; não a publique.
3. Para aplicar um IPS existente, escolha um caminho novo que ainda não exista: `python tools/apply_patch.py --rom "CAMINHO/DA/ROM-ORIGINAL.gba" --patch patches/Beyblade-AHEJ-English-v150-EXPERIMENTAL.ips --output "CAMINHO/DE/SAIDA.gba"`. A ferramenta confere o hash da origem e recusa sobrescrever a ROM ou outro arquivo existente.
4. Após mudar fontes, alinhe os metadados/notas de versão com o resultado real. Execute a revisão visual dos três casos de maior risco conforme as preferências acima; não descreva capturas com fixtures como confirmação de acionamento natural.

O build depende da ROM original fornecida pelo usuário. Nunca editar o arquivo original: todas as saídas devem ser novas cópias geradas em caminhos separados.

## GitHub

Descrição planejada do repositório:

> Fan-made English translation of Bakuten Shoot Beyblade: Gekitou! Saikyou Blader (GBA, AHEJ), developed with GPT assistance. Includes translation sources and patching tools; the original ROM is not included.

As notas de publicação registram que o projeto local ainda é um rascunho não publicado e que não há licença escolhida. Não afirmar que foi publicado ou licenciado sem confirmar o estado atual.

## Auditoria pendente

O grupo 2 já tem tradução nos 837 recursos com texto. A faixa de falas traduzidas do grupo 1 cobre as cenas 308–616. A cena 312 recebeu tradução e o construtor agora aceita a transição de texto sem falante inicial para um falante definido. Build/IPS v1.50 passou; a captura automática não chegou ao fixture de tradução. Os rótulos gráficos do menu inicial, hub e atributos do catálogo seguem pendentes. O layout natural dos menus estruturados e acionamentos naturais continuam sem verificação. Não afirmar cobertura integral nem publicação.
