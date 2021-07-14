def em_ambas(p1, p2):
    str_aux = p1.lower()
    for letra in str_aux:
        if letra in p2.lower():
            print("A letra", letra, "está na palavra", p2)
        else:
            print("A letra", letra, "não está na palavra", p2)


em_ambas("cAchorro", "gato")
