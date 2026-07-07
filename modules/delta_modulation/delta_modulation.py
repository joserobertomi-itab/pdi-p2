"""Compressão Delta Modulation (DM) — convenções da disciplina PDI.

Convenções:
- Varredura raster (linha a linha, esquerda -> direita).
- Seed: apenas o pixel (0,0) é transmitido intacto.
- Predição: pixel à esquerda; na 1ª coluna, o pixel de cima.
- Passo: +delta se x > predição, -delta se x < predição.
- Empate (x == predição): olha o PRÓXIMO valor da varredura e adota o
  passo que deixa a reconstrução mais perto dele; se as duas opções
  empatarem também, adota o passo mais favorável ao pixel atual.
- Saturação nos dois extremos: resultado fora de [vmin, vmax] trava na borda.
"""


def dm_encode(img, delta=2, vmin=0, vmax=4):
    """Retorna (reconstruída, MSE) da imagem (lista de listas) via DM."""
    h, w = len(img), len(img[0])
    clamp = lambda v: min(vmax, max(vmin, v))
    recon = [[0] * w for _ in range(h)]
    recon[0][0] = img[0][0]  # seed
    order = [(i, j) for i in range(h) for j in range(w)][1:]
    for k, (i, j) in enumerate(order):
        pred = recon[i][j - 1] if j > 0 else recon[i - 1][0]
        x = img[i][j]
        if x > pred:
            step = delta
        elif x < pred:
            step = -delta
        else:  # empate: lookahead no próximo valor da varredura
            nxt = img[order[k + 1][0]][order[k + 1][1]] if k + 1 < len(order) else x
            up, dn = clamp(pred + delta), clamp(pred - delta)
            if abs(up - nxt) != abs(dn - nxt):
                step = delta if abs(up - nxt) < abs(dn - nxt) else -delta
            else:  # empate do empate: favorece o pixel atual
                step = delta if abs(up - x) <= abs(dn - x) else -delta
        recon[i][j] = clamp(pred + step)
    se = sum((x - y) ** 2 for a, b in zip(img, recon) for x, y in zip(a, b))
    return recon, se / (h * w)


def demo():
    img = [
        [0, 3, 0, 3, 0],
        [2, 2, 0, 0, 3],
        [0, 0, 0, 0, 1],
        [3, 1, 1, 4, 2],
        [3, 3, 4, 4, 4],
    ]
    recon, mse = dm_encode(img)
    for row in recon:
        print(row)
    print("MSE =", mse)
    assert recon[4] == [4, 2, 4, 4, 4]
    assert mse == 17 / 25
    print("ok")


if __name__ == "__main__":
    demo()
