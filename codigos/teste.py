from aula12 import Calcado, Sandalia  # -> <elemento>

# import aula12 -> aula12.<elemento>

tenis1 = Calcado(40, "couro", 200.0)
tenis2 = Calcado(40, "couro", 200.0)
sandalia1 = Sandalia("marca", 40, "couro", 200.0)

# OS COMANDOS ABAIXO SÃO EQUIVALENTES
print(tenis1 + tenis2)
print(tenis1.__add__(tenis2))
#

print(tenis1)
print(sandalia1)
