"""Código de cadeia (chain code, Freeman) — convenções da disciplina PDI.

Convenções:
- 8 direções numeradas em sentido anti-horário: 0=E, 1=NE, 2=N, 3=NO,
  4=O, 5=SO, 6=S, 7=SE (coordenadas (x, y) com y para CIMA).
- Contorno percorrido em sentido anti-horário; o código tem um dígito
  por ponto do contorno (fecha no ponto inicial).
- Normalização (ponto de partida): rotação circular de menor valor inteiro.
- Invariância a rotação do objeto: primeira diferença ((d[i+1]-d[i]) mod 8),
  depois normalizar.
"""

DIRS = {(1, 0): 0, (1, 1): 1, (0, 1): 2, (-1, 1): 3,
        (-1, 0): 4, (-1, -1): 5, (0, -1): 6, (1, -1): 7}
STEP = {v: k for k, v in DIRS.items()}


def chain_code(path):
    """Código de cadeia do caminho fechado [(x,y), ...] (sem repetir o 1º ponto)."""
    return "".join(str(DIRS[(b[0] - a[0], b[1] - a[1])])
                   for a, b in zip(path, path[1:] + path[:1]))


def is_closed(code):
    """True se os deslocamentos do código somam zero (contorno fechado)."""
    dx = sum(STEP[int(c)][0] for c in code)
    dy = sum(STEP[int(c)][1] for c in code)
    return dx == 0 and dy == 0


def normalize(code):
    """Rotação circular que forma o menor inteiro (independe da partida)."""
    return min(code[i:] + code[:i] for i in range(len(code)))


def first_difference(code):
    """Primeira diferença (mod 8) — invariante a rotação do objeto."""
    return "".join(str((int(b) - int(a)) % 8)
                   for a, b in zip(code, code[1:] + code[:1]))


def same_object(code_a, code_b, rotation_invariant=False):
    if rotation_invariant:
        code_a, code_b = first_difference(code_a), first_difference(code_b)
    return normalize(code_a) == normalize(code_b)


def demo():
    # contorno da prova (anti-horario, a partir do ponto superior esquerdo)
    path = [(3, 6), (3, 5), (2, 4), (1, 3), (2, 2), (3, 1), (4, 0), (5, 0),
            (6, 0), (7, 0), (8, 0), (9, 1), (9, 2), (8, 2), (7, 2), (6, 2),
            (6, 3), (7, 4), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6)]
    code = chain_code(path)
    dado = "12244446557770000124442"
    print("codigo da imagem  :", code)
    print("normalizado       :", normalize(code))
    print("dado normalizado  :", normalize(dado))
    assert code == "65577700001244421224444"
    assert is_closed(code) and is_closed(dado)
    assert normalize(code) == normalize(dado) == "00001244421224444655777"
    assert same_object(code, dado)
    print("mesmo objeto: ok")


if __name__ == "__main__":
    demo()
