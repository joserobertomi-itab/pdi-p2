# PDI-P2 — Material de estudo (Processamento Digital de Imagens)

Repositório de estudo para a **2ª prova de Processamento Digital de Imagens**
(Ciência da Computação). Reúne resumos seção por seção dos livros e dos PDFs do
moodle, com figuras recortadas das fontes, organizados por um roadmap guiado pelas
questões das provas anteriores.

## 📍 Por onde começar

- **[`roadmap.md`](roadmap.md)** — mapa de estudo com o que caiu nas provas
  2024/2025 e o progresso por tópico.
- **[`notes/README.md`](notes/README.md)** — índice de todas as notas.

## 📚 Conteúdo (teoria completa)

| Módulo | Tópicos | Fonte |
|--------|---------|-------|
| 1 — Segmentação | 10.1 fundamentos · 10.2 bordas · 10.3 limiarização/Otsu · 10.4 região · 10.5 watersheds | Gonzalez cap. 10 |
| 2 — Bordas e contornos | 7.2 (escala, cor/textura, detector Pb, linking) | Szeliski 7.2 |
| 3 — Representação e descrição | 11.1 código de cadeia · 11.2.1 descritores · 11.3 textura · 11.4 PCA · 11.5 relacionais | Gonzalez cap. 11 |
| 4 — Compressão | 8.1 fundamentos (entropia, MSE, modelo) + motivação | Gonzalez 8.1 + moodle |
| 5 — JPEG | pipeline DCT → quantização → zig-zag → RLE → Huffman | moodle |
| 6 — Vídeo | I/P/B, GOP, compensação de movimento, artefatos | moodle |

## 🗂️ Estrutura

```
roadmap.md            # mapa de estudo + mapa das questões das provas
notes/                # resumos por seção (um arquivo por tópico) + figuras
  cap08/ cap10/ cap11/ szeliski/ moodle/
books/                # Gonzalez (2009), Szeliski (2022)
articles/             # PDFs do moodle (JPEG, compressão, vídeo)
tests/                # provas anteriores (2024, 2025)
```

## 🎯 Mapa das questões da prova

| Q | Tarefa | Nota de apoio |
|---|--------|---------------|
| 1a | Delta Modulation + MSE | [8.1](notes/cap08/8.1-fundamentos-compressao.md) · [compressão](notes/moodle/compressao-motivacao.md) |
| 1b | LBP (Local Binary Pattern) | [11.3](notes/cap11/11.3-descritores-regionais.md) |
| 2 | Artefato de vídeo (causa + solução) | [vídeo](notes/moodle/video.md) |
| 3 | Código de cadeia (normalizar + comparar) | [11.1](notes/cap11/11.1-representacao.md) · [11.2.1](notes/cap11/11.2.1-descritores-simples-fronteira.md) |
| 4 | PCA / reconhecimento facial | [11.4](notes/cap11/11.4-componentes-principais.md) |
| 5 | JPEG (DCT → quant → zig-zag → RLE) | [JPEG](notes/moodle/jpeg.md) |

---

*As notas resumem o conteúdo das fontes citadas para fins de estudo.*
