# Aplicativo de revisão local

Abra `Iniciar-Revisao.cmd` com dois cliques. A interface abre no navegador e usa apenas `127.0.0.1`, no próprio computador. Não chama serviços de IA, não envia capturas, não instala pacotes e não publica arquivos. A aba precisa permanecer aberta apenas para acompanhar; o processo local executa o trabalho.

## Uso

1. Escolha **Batalha** ou **História**.
2. Mantenha a amostra em **3**. “Maiores do grupo” testa os três maiores recursos codificados. “Alterados ainda não testados” compara com a última execução local e também inclui nomes dinâmicos e formatos sem cabeçalho alterados.
3. Para limitar a seleção ao lote atual, preencha o filtro de recursos (por exemplo, `738-779,783-785`). Deixe vazio para considerar todo o grupo. Clique em **Construir e verificar**.
4. Abra a galeria. Confira as imagens, marque **Aprovado** ou **Revisar** e, se quiser, exporte sua revisão em JSON.

Os caminhos da ROM original, do núcleo mGBA e dos estados já são detectados nesta pasta. Para outra instalação, edite a seção de arquivos locais. Batalha usa `launch-power.state`; história usa `battle-open.state`. Outros estados não são intercambiáveis: estes perfis dependem desses pontos específicos do jogo.

O lançador usa o Python e o Pillow já disponíveis neste computador. Em outra máquina, requer Python 3.12 com Pillow, uma cópia compatível de `mgba_libretro.dll`, a ROM original AHEJ e os estados privados apropriados. Nenhum desses binários faz parte do projeto publicável.

## O que é automático

- Reconstrução das traduções e verificação independente do IPS.
- Verificações de comandos, nomes, largura e alocação existentes nos inseridores.
- Seleção por tamanho dos recursos codificados.
- Execução do emulador em processos locais separados, usando cópias temporárias.
- Capturas, remoção de imagens exatamente idênticas na galeria e relatórios HTML/JSON.
- Na história, as capturas são espaçadas por 54 quadros (cerca de 0,9 s no tempo simulado a 60 fps); o emulador pode processar esses quadros mais rápido que o tempo real.
- Registro de recursos já executados. Mudanças no inseridor, emulador, núcleo ou estado invalidam esse registro.

Cada execução fica em `build/qa/<data-hora>/`. O registro completo da reconstrução fica em `build.log`; cada recurso tem seu próprio `emulator.log`. Os arquivos `.gba` nessa pasta são cópias de teste e podem conter substituições temporárias. A ROM traduzida de uso normal fica diretamente em `build/`.

## Limites

A amostra padrão usa os três maiores textos do lote; as verificações automáticas abrangem todas as traduções. Textos menores também podem apresentar erros próprios, mesmo quando os três maiores cabem.

“Execução concluída” não significa “texto visualmente aprovado”. O aplicativo não julga fidelidade ao japonês, cortes de texto, travamentos silenciosos, desempenho em hardware nem cobertura completa da campanha.

Os testes da história substituem o recurso de abertura. As continuações sem cabeçalho recebem um contexto de teste com o retrato de Kyouju. Os testes de batalha selecionam um fluxo no renderizador ativo usando RAM de teste. A ROM distribuída não recebe essas alterações de teste. Essas execuções não comprovam o acionamento natural das cenas.

As janelas de captura são limitadas, mas podem incluir a sequência seguinte. Imagens idênticas são ocultadas; imagens apenas parecidas permanecem. Quadros únicos ainda podem mostrar uma linha sendo revelada. A galeria não usa OCR nem declara ausência de erros a partir de imagens.

As marcações de revisão ficam no armazenamento do navegador, separadas por execução. O botão de exportação permite guardar uma cópia. O estado automático dos relatórios continua como **revisão visual pendente**.

**Cancelar após teste atual** termina depois do recurso em andamento; não interrompe a reconstrução nem o emulador no meio da gravação. **Encerrar aplicativo local** desliga o servidor quando não há trabalho ativo. Fechar apenas a aba deixa o servidor local ligado; abrir o lançador novamente reutiliza a instância.

As configurações, caminhos e registros locais ficam em `private/local-review/`, ignorado pelo Git. ROM, núcleo, estados e relatórios de teste permanecem fora do conteúdo publicável.

## Política de repetição

Cada amostra é executada uma vez. Repetir somente após falha ou correção relevante, com no máximo três tentativas por caso. Não repetir testes aprovados sem mudança que os afete.
