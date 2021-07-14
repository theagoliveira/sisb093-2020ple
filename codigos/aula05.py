import math


def area_circulo(raio):
    return math.pi * (raio ** 2)


def valor_absoluto(n):
    if isinstance(n, str):
        print("Tipo inválido para o número.")
        return None
    else:
        if n < 0:
            return -n

        if n >= 0:
            return n


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def distancia_pontos(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d_quadrado = (dx ** 2) + (dy ** 2)
    return math.sqrt(d_quadrado)


def distancia_pontos_simpl(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def divisivel(x, y):
    return x % y == 0
