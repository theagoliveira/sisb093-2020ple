def cortar(x):
    del x[0]
    del x[-1]


def cortar_2(x):
    return x[1:-1]


t = [1, 2, 3, 4]
t = cortar_2(t)
print(t)
