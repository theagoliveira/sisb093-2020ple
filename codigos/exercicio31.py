def alinhar_direita(s, c):
    qtd_espacos = c - len(s)
    resultado = (" " * qtd_espacos) + s
    print(resultado)


alinhar_direita("ufal", 5)
alinhar_direita("ufal", 10)
