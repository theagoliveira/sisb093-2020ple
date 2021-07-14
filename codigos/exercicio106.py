def checar_anagrama(a, b):
    lista_a = list(a)
    lista_b = list(b)
    lista_a.sort()
    lista_b.sort()
    return lista_a == lista_b


print(checar_anagrama("abcdf", "bcaxd"))
