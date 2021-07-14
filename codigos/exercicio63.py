def primeira_letra(palavra):
    return palavra[0]


def ultima_letra(palavra):
    return palavra[-1]


def meio(palavra):
    return palavra[1:-1]


def checar_palindromo(palavra):
    str_aux = palavra
    while len(str_aux) > 0:
        if primeira_letra(str_aux) != ultima_letra(str_aux):
            return False
        str_aux = meio(str_aux)
    return True


print(checar_palindromo("reviver"))
print(checar_palindromo("abcdefg"))
