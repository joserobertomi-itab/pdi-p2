# Respostas P2 2024

## Pergunta 4 — Agrupar fotos de pontos turísticos (0,5)

**Enunciado:** João deseja agrupar fotos em dois grupos, cada um representando um ponto turístico. Como entrada ele recebe dezenas de fotos de pontos turísticos. Descreva todo o processo, utilizando os algoritmos vistos em sala, entradas e saídas, para resolver o problema em questão. (O dataset de exemplo possui fotos adquiridas em diversas posições e em diversos momentos do dia — ex.: Torre Eiffel e um pavilhão circular, cada um fotografado de ângulos e horários diferentes.)

**Resposta objetiva:** o problema é de **agrupamento não supervisionado** com `k = 2`, e o ponto central é a escolha da representação: as fotos variam em **posição/ângulo e iluminação**, então a comparação deve usar **descritores locais invariantes** (ex.: **SIFT** ou **ORB**, vistos em sala) — invariantes a escala, rotação e parcialmente a iluminação. O pipeline: extrair keypoints e descritores de cada foto → casar descritores entre pares de fotos (*matching*) → montar uma matriz de similaridade (nº de bons matches) → agrupar em 2 clusters. Fotos do mesmo monumento compartilham muita estrutura local (muitos matches); monumentos diferentes, quase nenhuma.

### O processo, etapa por etapa

#### Etapa 1 — Extração de características locais

- **Entrada:** N fotos, em resoluções, ângulos e iluminações variadas (nenhum alinhamento exigido).
- **Processo:** para cada foto, um detector+descritor (ex.: **SIFT** ou **ORB**) localiza os **keypoints** (pontos salientes: cantos, quinas da torre, bordas da cúpula) e calcula para cada um um **descritor** — um vetor que codifica a vizinhança do ponto de forma **invariante a escala e rotação** e robusta a mudanças de iluminação. É essa invariância que absorve o "diversas posições e diversos momentos do dia" do enunciado.
- **Saída:** N conjuntos de descritores (centenas de vetores por foto).

#### Etapa 2 — Matching entre pares de fotos

- **Entrada:** os N conjuntos de descritores.
- **Processo:** para cada par de fotos (i, j), casar os descritores (vizinho mais próximo por distância entre vetores, filtrando ambiguidades com o *ratio test*). O número de **bons matches** mede a similaridade: duas fotos da Torre Eiffel, mesmo de ângulos e horários diferentes, compartilham dezenas/centenas de pontos correspondentes; uma foto da torre contra o pavilhão, praticamente nenhum. Com dezenas de fotos, o custo O(N²) de pares é irrelevante.
- **Saída:** matriz de similaridade N×N (nº de bons matches por par).

#### Etapa 3 — Agrupamento em 2 grupos

- **Entrada:** a matriz de similaridade e `k = 2`.
- **Processo:** como os dois monumentos são bem separados, basta **limiarizar** a similaridade e agrupar as fotos que se conectam (componentes conexos: quem tem muitos matches entre si fica no mesmo grupo). Alternativamente, um agrupamento padrão (hierárquico ou K-means com k=2) sobre a matriz produz o mesmo resultado.
- **Saída:** um rótulo (0 ou 1) para cada foto — dois clusters.

#### Etapa 4 — Resultado

- **Saída final:** dois grupos de fotos, um por ponto turístico (ex.: cluster A = fotos da Torre Eiffel, cluster B = fotos do pavilhão circular), independentemente do ângulo e do horário em que cada foto foi tirada.

**Resumo para a prova:** **pipeline** = extração de características locais invariantes (**SIFT/ORB**: keypoints + descritores) → **matching** par a par (bons matches = similaridade) → **agrupamento** em 2 clusters (limiar/K-means sobre a matriz de similaridade) → dois grupos, um por monumento. Entrada de cada etapa = saída da anterior; a robustez a posição e iluminação vem da **invariância dos descritores locais**, que é exatamente o que o dataset do enunciado exige.
