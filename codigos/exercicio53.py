def checar_triangulo(a, b, c):
    cond1 = (a + b) > c
    cond2 = (a + c) > b
    cond3 = (b + c) > a
    cond_final = cond1 and cond2 and cond3
    if cond_final:
        print("triangulo pode ser formado.")
    else:
        print("triangulo não pode ser formado.")


def entrada_usuario():
    x = int(input("Digite o primeiro lado: "))
    y = int(input("Digite o segundo lado:  "))
    z = int(input("Digite o terceiro lado: "))
    checar_triangulo(x, y, z)


entrada_usuario()
