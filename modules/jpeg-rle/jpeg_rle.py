"""RLE dos coeficientes AC no JPEG (pos DCT + quantizacao + zig-zag).

Convenções:
- O 1º valor do bloco é o DC (codificado à parte, por DPCM) — o RLE
  atua só nos AC.
- Cada AC não-nulo vira o par (RUN, VALOR), onde RUN = nº de zeros
  imediatamente antes dele.
- Cauda de zeros até o fim do bloco vira um único EOB = (0, 0).
  Se o último coeficiente é não-nulo, não há EOB.
- SIZE (categoria) da amplitude v: nº de bits de |v|  (±1→1, ±2..3→2,
  ±4..7→3, ±8..15→4, ...). Custo aproximado de um par: bits do Huffman
  de (RUN, SIZE) + SIZE bits da amplitude.
"""

EOB = (0, 0)


def rle_ac(block):
    """RLE dos AC de um bloco em zig-zag (block[0] = DC). Retorna lista de pares."""
    ac = block[1:]
    pares, run = [], 0
    for v in ac:
        if v == 0:
            run += 1
        else:
            pares.append((run, v))
            run = 0
    if run:  # sobrou cauda de zeros
        pares.append(EOB)
    return pares


def size(v):
    """Categoria SIZE da amplitude (nº de bits de |v|)."""
    return abs(v).bit_length()


def bits_estimados(pares, huffman_par=4):
    """Estimativa: cada par custa ~huffman_par bits de Huffman + SIZE bits."""
    # ponytail: huffman fixo em 4 bits/par; use as tabelas do padrao se precisar do valor exato
    return sum(huffman_par + size(v) for _, v in pares if (_, v) != EOB) \
        + (huffman_par if EOB in pares else 0)


def demo():
    A = [10, -5, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1]
    ra, rb = rle_ac(A), rle_ac(B)
    print("Bloco A:", ra, f"-> {len(ra)} simbolos, ~{bits_estimados(ra)} bits")
    print("Bloco B:", rb, f"-> {len(rb)} simbolos, ~{bits_estimados(rb)} bits")
    assert ra == [(0, -5), (2, 2), EOB]
    assert rb == [(0, v) for v in B[1:]] and EOB not in rb
    assert bits_estimados(ra) < bits_estimados(rb)
    print("ok: bloco A tem fluxo de bits menor")


if __name__ == "__main__":
    demo()
