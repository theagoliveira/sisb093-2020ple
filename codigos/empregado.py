from exercicio122 import Endereco


class Empregado:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
        self._endereco = None

    def __repr__(self):
        return f"Nome: {self._nome}, Salário: {self._salario}"

    def set_endereco(self, num, rua, cidade, estado, cep, apt=""):
        self._endereco = Endereco(num, rua, cidade, estado, cep, apt)


emp1 = Empregado("Thiago", 1000.0)
emp1.set_endereco("10", "Rua Sem Nome", "Penedo", "Alagoas", "55566-777")
print(emp1)
emp1._endereco.imprimir()
