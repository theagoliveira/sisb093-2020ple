# string = "abcdef"
# indice = 0
# # TRAVESSIA DE STRING COM WHILE
# while indice < len(string):
#     caractere = string[indice]
#     # COMEÇO DO PROCESSAMENTO
#     print("caractere:", caractere)
#     # FIM DO PROCESSAMENTO
#     indice = indice + 1

# # TRAVESSIA DE STRING COM FOR
# for caractere in string:
#     print("caractere:", caractere)

# prefixos = "MGPR"
# sufixo = "ato"
# for letra in prefixos:
#     if letra != "P":
#         print(letra + sufixo)
#     else:
#         print(letra + "r" + sufixo)


def buscar(palavra, letra, indice_inicial):
    indice = indice_inicial
    while indice < len(palavra):
        if palavra[indice] == letra:
            return indice
        indice = indice + 1
    return -1


# string = "abcdef"
# letra_1 = "d"
# letra_2 = "k"

# resultado = buscar(string, letra_1, 4)
# if resultado == -1:
#     print("A letra", letra_1, "não está presente na string")
# else:
#     print("A letra", letra_1, "está presente na string, no índice", resultado)

# resultado = buscar(string, letra_2, 4)
# if resultado == -1:
#     print("A letra", letra_2, "não está presente na string")
# else:
#     print("A letra", letra_2, "está presente na string, no índice", resultado)


def contar(palavra, letra):
    contador = 0
    for i in palavra:
        if i == letra:
            contador = contador + 1
    return contador


string = "asdhgudbatfgaa"
caractere = "a"
resultado = contar(string, caractere)
print("A palavra", string, "possui", resultado, "letras a.")
