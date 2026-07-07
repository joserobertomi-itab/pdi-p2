# Respostas P2 2025

## Pergunta 2 — Artefatos em transmissão de vídeo

**Enunciado:** Em uma transmissão de um vídeo, um aluno notou os artefatos exibidos na figura (A), que demonstra um pequeno trecho de um vídeo. Explique o artefato, porque ele ocorre e indique uma solução para amenizar o problema.

*(Figura A = Fig. 1 do paper "Transmission Distortion Modeling for Wireless Video Communication", Dani, He & Hongkai, IEEE GLOBECOM 2005 — `papers/Transmission_distortion_modeling_for_wireless_vide.pdf`)*

**Resposta objetiva:** o artefato da figura é a **propagação e acumulação de erro de transmissão** (*error propagation / drift*): blocos corrompidos que aparecem em um quadro e se espalham/persistem nos quadros seguintes. Ele ocorre porque a perda de pacotes no canal sem fio corrompe um quadro que serve de **referência para a predição por movimento** dos quadros seguintes — o erro "viaja" pelas cadeias de predição. A solução clássica é a **atualização intra** (inserir quadros/blocos I periodicamente), que quebra a cadeia de predição e faz o erro desaparecer.

### Progressão de conteúdo

#### 1. Como o vídeo é comprimido: predição temporal

Vídeo tem enorme redundância temporal — quadros consecutivos são quase iguais. Os codecs exploram isso codificando a maioria dos quadros como **quadros P (preditos)**: em vez de transmitir o quadro inteiro, transmite-se só a diferença em relação ao quadro anterior, usando **compensação de movimento** (cada bloco do quadro atual é "apontado" para um bloco parecido do quadro anterior). A estrutura típica é um quadro **Intra (I)** — autocontido — seguido de uma longa sequência de quadros P, exatamente a estrutura usada no paper.

Consequência estrutural: **cada quadro P depende do quadro anterior estar correto**. Essa dependência em cadeia é a raiz do artefato.

#### 2. O canal sem fio é propenso a erros

No canal wireless, variante no tempo, cada pacote de vídeo pode chegar correto, chegar com erros de bit ou ser perdido. Bits errados causam falha de decodificação e o decodificador é obrigado a **descartar os dados daquele pacote**. Para não deixar um "buraco" na tela, ele aplica **error concealment** (ocultação de erro) — tipicamente copia os pixels da mesma região do quadro anterior decodificado. Isso disfarça, mas não recupera a informação perdida: nasce ali uma distorção, os blocos visivelmente errados da figura.

#### 3. Por que o erro se espalha: propagação pela cadeia de predição

Aqui está o mecanismo central que a Fig. 1 ilustra. O quadro corrompido no instante `n₀` vira **referência** para o quadro `n₀+1`, que vira referência para o `n₀+2`, e assim por diante. O erro introduzido em um único quadro **propaga-se ao longo dos caminhos de predição de movimento** e se **acumula** com novos erros do canal — mesmo que todos os quadros seguintes cheguem perfeitos, eles são reconstruídos a partir de uma referência já errada. É por isso que na figura os artefatos não somem: eles persistem e se deslocam acompanhando o movimento da cena, degradando a qualidade ao longo do tempo.

O paper formaliza isso definindo a distorção de transmissão como `Dₜ(n) = E{[F̂(n,i) − F̃(n,i)]²}` — o erro quadrático médio entre a reconstrução do codificador e a do decodificador — e mostra que a resposta a um erro impulsivo decai como uma exponencial `H(n) = Dₜ(n₀)·e^(−α(n−n₀))`, onde o fator de desvanecimento `α` depende de quanto cada quadro é predito do anterior (o *motion reference ratio*).

#### 4. Como amenizar

Da própria mecânica do problema saem as soluções — todas atacam a cadeia de dependência ou a perda em si:

- **Intra refresh (principal):** inserir quadros I periodicamente, ou atualizar blocos em modo intra de forma distribuída (*adaptive intra block update*). Um quadro/bloco I não depende de referência nenhuma, então **corta a cadeia de propagação** e "zera" o erro acumulado. É o compromisso clássico: quadros I custam mais bits, mas limitam o alcance temporal de qualquer erro.
- **Proteção contra a perda:** FEC (códigos corretores de erro) ou retransmissão (ARQ) nos pacotes mais importantes, reduzindo a chance de o erro entrar.
- **Alocação inteligente de recursos** — a contribuição do paper: com o modelo preditivo de distorção, o codificador estima antecipadamente quanto uma perda vai custar em qualidade e aloca bits/energia/modo de codificação (inter vs. intra) para minimizar a distorção esperada no receptor.

**Resumo para a prova:** **artefato** = propagação/acumulação de erro por perda de pacotes; **causa** = predição por compensação de movimento encadeia os quadros, então a referência corrompida contamina os seguintes; **solução** = intra refresh (quadros/blocos I periódicos) para quebrar a cadeia — opcionalmente citando FEC e error concealment como medidas complementares.

---

## Pergunta 4 — Reconhecimento facial lento (0,6)

**Enunciado:** Uma rede de academias decidiu modernizar seu sistema de controle de acesso por um sistema de reconhecimento facial. Para cada novo aluno, o sistema armazena uma foto de rosto em alta resolução (2048×2048 pixels). Quando um aluno se aproxima da câmera na entrada, o sistema captura uma nova imagem. Em seguida, para realizar a identificação, o programa carrega a imagem recém-capturada e, sequencialmente, processa cada uma das armazenadas no servidor. Para cada par de imagens (a atual e uma da base), o sistema extrai as características faciais de ambas usando um algoritmo robusto e calcula uma pontuação de similaridade. Se a pontuação ultrapassar um limiar para qualquer imagem da base, o acesso é liberado, interrompendo o processo. Nos testes, com o aluno Alan o processo foi rápido, mas com a aluna Vanessa a identificação levou 30 segundos. Proponha uma alternativa e explique como sua proposta resolve especificamente o problema de tempo de identificação.

**Resposta objetiva:** o gargalo é que o sistema **re-extrai as características faciais das imagens da base a cada identificação**. A extração de características (a etapa cara, feita sobre imagens de 2048×2048) é executada N vezes por tentativa de acesso, sendo N o tamanho da base — e como a busca é sequencial com parada no primeiro match, quem está no início da lista (Alan) sai rápido e quem está no fim (Vanessa) paga o custo quase completo. A solução é **pré-computar as características uma única vez no cadastro** e armazenar apenas os vetores de características (*embeddings*); na entrada, extrai-se características **só da imagem capturada** e compara-se vetor contra vetor, o que é ordens de grandeza mais barato.

### Construindo a resposta

#### 1. Diagnóstico: onde o tempo é gasto

Por tentativa de acesso, o custo atual é aproximadamente:

```text
tempo ≈ k × (2 × custo_extração + custo_comparação)
```

onde `k` é a posição do aluno na varredura sequencial. Dois problemas se compõem:

1. **Trabalho redundante:** as fotos da base são fixas — extrair suas características de novo a cada acesso é recomputar sempre o mesmo resultado. É o custo dominante: um algoritmo "robusto" sobre imagens de 4 megapixels é muito mais caro que comparar dois vetores.
2. **Busca linear com parada antecipada:** o tempo depende da posição do aluno na base. Alan estava no começo; Vanessa, perto do fim — daí os 30 segundos. O sistema não escala: dobrou a base, dobrou o pior caso.

#### 2. Proposta: pré-computação dos vetores de características (enrollment offline)

Reestruturar o sistema em duas fases:

- **Fase de cadastro (uma vez por aluno):** ao matricular, o sistema extrai as características faciais da foto e armazena **o vetor de características** (tipicamente algumas centenas de valores, ex.: 128–512 floats) junto ao registro do aluno. A foto em alta resolução deixa de participar da identificação.
- **Fase de identificação (a cada acesso):** o sistema extrai características **apenas da imagem recém-capturada (1 extração, não N)** e calcula a similaridade (ex.: distância euclidiana ou cosseno) contra os vetores já armazenados.

O custo por acesso cai para:

```text
tempo ≈ 1 × custo_extração + N × custo_comparação_de_vetores
```

Comparar dois vetores de ~512 números custa microssegundos — mesmo varrendo a base inteira, o tempo fica dominado por **uma única extração**, igual para Alan e para Vanessa. É exatamente isso que resolve o problema relatado: o tempo de identificação deixa de depender da posição do aluno na base e do tamanho da base multiplicado pelo custo de extração.

#### 3. Refinamento opcional (se a base crescer muito)

Para milhares de unidades/alunos, a varredura linear dos vetores também pode ser eliminada com **indexação para busca por similaridade** (ex.: k-d tree ou índices de vizinho mais próximo aproximado, como ANN/FAISS), reduzindo a busca de O(N) para aproximadamente O(log N). Reduções auxiliares também ajudam: detectar e recortar a região do rosto e redimensionar antes da extração — não há necessidade de processar 2048×2048 inteiros para reconhecimento facial.

**Resumo para a prova:** **problema** = extração de características repetida N vezes sobre a base a cada acesso + busca sequencial (tempo depende da posição do aluno — Alan cedo, Vanessa tarde). **Proposta:** pré-computar e armazenar os vetores de características no cadastro; na identificação, extrair características só da imagem capturada e comparar vetores. **Por que resolve:** o custo cai de N extrações caras para 1 extração + N comparações triviais, tornando o tempo praticamente constante e independente da posição/tamanho da base.
