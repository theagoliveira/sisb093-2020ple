import math


class LataRefrigerante:
    def __init__(self, altura, raio):
        self.altura = altura
        self.raio = raio

    def areaSupericie(self):
        areaBase = math.pi * (self.raio ** 2)
        areaCorpo = self.altura * (2 * math.pi * self.raio)

        return 2 * areaBase + areaCorpo

    def volume(self):
        areaBase = math.pi * (self.raio ** 2)

        return areaBase * self.altura


lata = LataRefrigerante(10.0, 5.0)
print(lata.areaSupericie())
print(lata.volume())
