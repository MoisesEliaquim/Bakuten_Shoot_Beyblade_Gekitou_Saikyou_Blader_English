# Beyblade: Gekitou! Saikyou Blader — tradução para inglês

Projeto experimental de tradução do primeiro **Bakuten Shoot Beyblade — Gekitou! Saikyou Blader**, de Game Boy Advance. A versão japonesa compatível usa o código **AHEJ**.

Este projeto experimental inclui o patch IPS, fontes editáveis e ferramentas. Foi desenvolvido com auxílio do GPT. A ROM original, emulador e saves não estão incluídos.

## Estado atual

- 587 falas traduzidas em 308 cenas.
- 816 textos de interface traduzidos.
- 62 opções estruturadas de local, loja e navegação em 28 recursos.
- 837 recursos de batalha em 1.259 páginas.
- Fonte estreita com até 24 caracteres por linha e páginas extras.
- Nomes japoneses e ordem dos personagens preservados.

A tradução é parcial. Alguns menus gráficos, nomes de peças e outros textos continuam em japonês. A revisão visual é parcial e o jogo completo ainda não foi testado. Consulte o [progresso e a cobertura dos testes](docs/PROGRESS.md).

## Aplicativo local de revisão

Abra `Iniciar-Revisao.cmd` com dois cliques. O aplicativo reconstrói a ROM, verifica o IPS e gera uma galeria local dos maiores textos para revisão, sem enviar capturas para uma IA. As configurações desta máquina já são detectadas. Consulte as [instruções e limitações](docs/LOCAL-APP.pt-BR.md).

## Aplicar o patch

Use Python 3.10 ou mais recente e sua própria ROM japonesa original, sem modificações. O programa cria uma cópia e não sobrescreve arquivos existentes.

```sh
python tools/apply_patch.py --rom "/caminho/original.gba" --patch patches/Beyblade-AHEJ-English-v150-EXPERIMENTAL.ips --output "/caminho/Beyblade-English-v150.gba"
```

SHA-256 exigido para a ROM original:

```text
58b7ad86fae87e572e8474eb935ecda165e71c741096cd687f96bed96fbba05c
```

Para gerar a tradução a partir dos arquivos editáveis:

```sh
python tools/build.py --rom "/caminho/original.gba"
```

O resultado fica em `build/`. O processo confere a ROM original e verifica se o patch reconstrói exatamente a ROM traduzida.

## Como ajudar

Registre versão do patch, emulador, personagem, etapa e passos para reproduzir o problema. Uma captura completa da caixa de diálogo ajuda. Não envie ROMs, executáveis de emuladores ou save states ao repositório.

Os arquivos editáveis estão em `translations/`. A [documentação técnica](docs/FORMAT.md) explica as tabelas, os comandos conhecidos e a fonte. A [documentação principal em inglês](README.md) contém mais informações para colaboradores.
