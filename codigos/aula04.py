escolha = "k"

if escolha == "a":
    print("usuário escolheu a.")
elif escolha == "b":
    print("usuário escolheu b.")
elif escolha == "c":
    print("usuário escolheu c.")
elif escolha == "d":
    print("usuário escolheu d.")
else:
    print("opção inválida.")

x = 8
y = 9

# Condicionais encadeadas (elif)
if x > y:
    print("x maior que y.")
elif x < y:
    print("x menor que y.")
else:
    print("x igual a y.")

# Condicionais aninhadas (if dentro de outro if)
if x == y:
    print("x igual a y.")
else:
    if x > y:
        print("x maior que y.")
    else:
        print("x menor que y.")
