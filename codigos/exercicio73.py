import math


def estimar_pi():
    c = 2 * math.sqrt(2) / 9801
    k = 0
    termo = (math.factorial(4 * k) * (1103 + 26390 * k)) / (
        (math.factorial(k) ** 4) * (396 ** (4 * k))
    )
    somatorio = termo
    while termo >= 10 ** -15:
        k = k + 1
        termo = (math.factorial(4 * k) * (1103 + 26390 * k)) / (
            (math.factorial(k) ** 4) * (396 ** (4 * k))
        )
        somatorio = somatorio + termo
    return 1.0 / (somatorio * c)


print(math.pi)
print(estimar_pi())
