import math


class EquacaoSegundoGrau:
    # FORMA: a * (x ** 2) + b * x + c
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._delta = (b ** 2) - 4 * a * c

    def imprimir_equacao(self):
        print(f"{self._a} * (x ** 2) + {self._b} * x + {self._c}")

    def raizes(self):
        if self._delta < 0:
            print("Não tem raízes reais.")
            return None
        elif self._delta == 0:
            return -self._b / (2 * self._a)
        else:
            x1 = (-self._b + math.sqrt(self._delta)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(self._delta)) / (2 * self._a)
            return (x1, x2)


x = EquacaoSegundoGrau(1, 5, 6)
x.imprimir_equacao()
print(x.raizes())
