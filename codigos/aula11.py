def conta_letras(texto):
    resultado = dict()
    for letra in texto:
        resultado[letra] = resultado.get(letra, 0) + 1
    return resultado


def imprimir_dicionario(d):
    for chave in sorted(d):
        print("Chave:", chave, "; Valor:", d[chave])


def busca(d, c):
    return d[chave]


def busca_reversa(d, v):
    for chave in sorted(d):
        if d[chave] == v:
            return chave
    return None


# print(conta_letras("aabbbccppzz"))
# imprimir_dicionario({"z": 2, "s": 3, "d": 4, "q": 5, "o": 7})
x = busca_reversa({"z": 2, "s": 3, "d": 4, "q": 4, "o": 4}, 3)
if x == None:
    print("Chave não encontrada.")
else:
    print("Chave:", x)
