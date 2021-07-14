preco = 24.95
desconto = 0.40
transp_primeiro = 3.00
transp_restante = 0.75
copias = 60

custo_livros = copias * preco * desconto
custo_transp = transp_primeiro + (copias - 1) * transp_restante

custo_total = custo_livros + custo_transp

print("custo_total:")
print(custo_total)
