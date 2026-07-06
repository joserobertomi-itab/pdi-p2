# Roadmap de estudo — Prova PDI P2

Materiais no repo:
- `books/gonzalez-2009.pdf` — Gonzalez & Woods, *Processamento Digital de Imagens*, 3ª ed. (PT-BR)
- `books/Szeliski-2022.pdf` — Szeliski, *Computer Vision: Algorithms and Applications*, 2ª ed. (EN)
- `articles/Slides JPEG ... UNIOESTE 2008.pdf` — Slides JPEG (moodle)
- `articles/video-formats-en.pdf` — Compressão de vídeo (moodle)
- `articles/silo.tips_...compressao-de-dados...pdf` — Motivação / compressão de dados (moodle)

Provas anteriores: `tests/ProvaP2-2024docx.pdf` e `tests/prova2025p2.pdf` (quase idênticas).

Legenda: `[ ]` a estudar · `[~]` em andamento · `[x]` compreendido · ~~riscado~~ = **fora da prova**

---

## 🎯 O que caiu nas provas 2024/2025 (prioridade máxima)

A prova é **prática/computacional**. As 5 questões se repetiram quase iguais nos dois anos:

| Q | Tarefa exigida | Onde estudar |
|---|----------------|--------------|
| 1a | **Delta Modulation** (+2=0, -2=1) e calcular o **MSE** | Módulo 4 (compressão preditiva + 8.1.5 fidelidade) |
| 1b | **LBP** — Local Binary Pattern de um pixel | Módulo 3 → 11.3.3 Textura |
| 2 | Explicar **artefato de vídeo**, causa e solução | Módulo 6 (vídeo) |
| 3 | **Normalizar código de cadeia** (anti-horário, 8 direções) + comparar 2 objetos | Módulo 3 → 11.1.2 + nº do formato |
| 4 | Agrupar fotos / acelerar reconhecimento facial (base grande) | Módulo 3 → **11.4 PCA/eigenfaces** + K-means |
| 5 | **JPEG**: DCT→quantização→zig-zag→**RLE**, contar bits, comparar blocos | Módulo 5 (JPEG) |

> Foco: dominar **fazer na mão** cada um desses 6 procedimentos. O resto do roadmap é a base teórica que sustenta essas respostas.

---

## Módulo 1 — Segmentação de imagens (Gonzalez cap. 10)  `[x] completo`

- [x] **10.1** Fundamentos (p. 455) — descontinuidade vs. similaridade → [notas](notes/cap10/10.1-fundamentos.md)
- [x] **10.2** Detecção de ponto, linha e borda (p. 456) → [notas](notes/cap10/10.2-deteccao-ponto-linha-borda.md)
  - 10.2.1 Fundamentos · 10.2.2 Pontos isolados · 10.2.3 Linhas
  - 10.2.4 Modelos de borda · 10.2.5 Detecção básica de bordas
  - 10.2.6 Técnicas avançadas (Marr-Hildreth, Canny) · 10.2.7 Ligação de bordas / Hough
- [x] **10.3** Limiarização / *thresholding* (p. 486) → [notas](notes/cap10/10.3-limiarizacao.md)
  - 10.3.1 Fundamentos · 10.3.2 Global simples · **10.3.3 Otsu**
  - 10.3.4 Suavização · 10.3.5 Usando bordas · 10.3.6 Múltiplos · 10.3.7 Variável · 10.3.8 Outras
- [x] **10.4** Segmentação baseada na região (p. 502) → [notas](notes/cap10/10.4-segmentacao-por-regiao.md)
  - 10.4.1 Crescimento de região · 10.4.2 Divisão e fusão (*split & merge*)
- [x] **10.5** Segmentação por *watersheds* (p. 506) → [notas](notes/cap10/10.5-watersheds.md)
  - Barragens · algoritmo · uso de marcadores

## Módulo 2 — Bordas e contornos (Szeliski 7.2)  `[x] completo`

- [x] **7.2** Edges and contours (p. 455) — complementa 10.2 → [notas](notes/szeliski/7.2-edges-and-contours.md)
  - 7.2.1 Edge detection · 7.2.2 Contour detection · 7.2.3 Edge editing/enhancement

## Módulo 3 — Representação e descrição (Gonzalez cap. 11)  `[x] completo`

- [x] **11.1** Representação (p. 523) → [notas](notes/cap11/11.1-representacao.md)
  - 11.1.1 Seguidor de fronteira · 11.1.2 Códigos da cadeia · 11.1.3 Aprox. poligonal
  - 11.1.4 Outras aproximações · 11.1.5 Assinaturas · 11.1.6 Segmentos de fronteira
  - ~~11.1.7 Esqueletos~~ **(fora)**
- [x] **11.2.1** Descritores de fronteira — alguns descritores simples (p. 537) → [notas](notes/cap11/11.2.1-descritores-simples-fronteira.md)
- [x] **11.3** Descritores regionais (p. 541) → [notas](notes/cap11/11.3-descritores-regionais.md)
  - 11.3.1 Simples · 11.3.2 Topológicos · 11.3.3 Textura
  - ~~11.3.4 Momentos invariantes~~ **(fora)**
- [x] **11.4** Uso de componentes principais (PCA) na descrição → [notas](notes/cap11/11.4-componentes-principais.md)
- [x] **11.5** Descritores relacionais → [notas](notes/cap11/11.5-descritores-relacionais.md)

## Módulo 4 — Fundamentos de compressão de imagens (Gonzalez 8.1 + moodle)  `[x] completo`

- [x] **8.1** Fundamentos (p. 348) → [notas](notes/cap08/8.1-fundamentos-compressao.md)
  - 8.1.1 Redundância de codificação · 8.1.2 Redundância espacial/temporal
  - 8.1.3 Informações irrelevantes · 8.1.4 Medindo informação (entropia)
  - 8.1.5 Critérios de fidelidade · 8.1.6 Modelos de compressão · 8.1.7 Padrões de formato
- [x] **Moodle** — motivação / compressão de dados → [notas](notes/moodle/compressao-motivacao.md)

## Módulo 5 — JPEG (moodle)  `[x] completo`

- [x] Slides JPEG UNIOESTE — DCT, quantização, zig-zag, Huffman, cadeia completa → [notas](notes/moodle/jpeg.md)

## Módulo 6 — Compressão de vídeo (moodle)  `[x] completo`

- [x] `video-formats-en.pdf` — redundância temporal, compensação de movimento, MPEG → [notas](notes/moodle/video.md)

---

**Ordem sugerida:** 1 → 2 → 3 → 4 → 5 → 6 (analisar a imagem antes de comprimir).
Vamos tópico por tópico; marque `[x]` conforme fecharmos cada um.
