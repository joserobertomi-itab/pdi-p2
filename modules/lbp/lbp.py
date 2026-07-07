"""LBP (Local Binary Pattern) — versão de prova: vizinhança 3x3 na grade.

Convenções:
- Vizinho >= centro -> bit 1, senão 0 (empate conta como 1, def. clássica).
- Leitura em sentido horário começando no canto superior esquerdo:
  TL, T, TR, R, BR, B, BL, L — primeiro bit lido é o mais significativo.
- Pixels de borda (sem 8 vizinhos) não são calculados.

Equivale ao local_binary_pattern(img, P=8, R=1) do skimage, exceto que o
skimage amostra num círculo (interpola as diagonais) e usa outra ordem de
leitura — o padrão de bits é o mesmo, só o decimal pode diferir.
"""

# deslocamentos (di, dj) em sentido horário a partir do canto superior esquerdo
OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def lbp_pixel(img, i, j):
    """LBP do pixel (i, j) (índices 0-based). Retorna (bits, decimal)."""
    c = img[i][j]
    bits = "".join("1" if img[i + di][j + dj] >= c else "0" for di, dj in OFFSETS)
    return bits, int(bits, 2)


def lbp_image(img):
    """LBP de toda a imagem; bordas ficam como None."""
    h, w = len(img), len(img[0])
    return [[lbp_pixel(img, i, j)[1] if 0 < i < h - 1 and 0 < j < w - 1 else None
             for j in range(w)] for i in range(h)]


def demo():
    img = [
        [0, 3, 0, 3, 0],
        [2, 2, 0, 0, 3],
        [0, 0, 0, 0, 1],
        [3, 1, 1, 4, 2],
        [3, 3, 4, 4, 4],
    ]
    # os dois pixels U (=0): todo vizinho >= 0, logo 11111111 = 255
    assert lbp_pixel(img, 1, 2) == ("11111111", 255)
    assert lbp_pixel(img, 1, 3) == ("11111111", 255)
    # pixel P=4 em (3,3): so a linha de baixo (4,4,4) >= 4
    assert lbp_pixel(img, 3, 3) == ("00001110", 14)
    for row in lbp_image(img):
        print(row)
    print("ok")


if __name__ == "__main__":
    demo()
