def soma_listas(x):
    soma = 0
    # PERCORRE LISTA EXTERNA
    for lista in x:
        # PERCORRE LISTA INTERNA
        for numero in lista:
            # ACUMULA O NUMERO NA SOMA
            soma = soma + numero
    return soma


t = [[1, 1], [2, 2], [3, 3]]
print(soma_listas(t))
