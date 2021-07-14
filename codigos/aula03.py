def repetir_frases():
    imprimir_frases()
    imprimir_frases()


def imprimir_frases():
    print("Frase 1.")
    print("Frase 2.")


def imprimir_duas_vezes(frase):
    print(frase)
    print(frase)


def concat_impr_duas_vezes(frase1, frase2):
    concatenacao = frase1 + frase2
    imprimir_duas_vezes(concatenacao)


concat_impr_duas_vezes()
