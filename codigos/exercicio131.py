class Pessoa:
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nasc = nasc

    def __repr__(self):
        return (
            f"Pessoa de nome {self._nome} e data de nascimento {self._nasc}."
        )


class Estudante(Pessoa):
    def __init__(self, nome, nasc, curso):
        super().__init__(nome, nasc)
        self._curso = curso

    def __repr__(self):
        return f"Estudante de nome {self._nome}, data de nascimento {self._nasc}, que faz o curso de {self._curso}."


class Professor(Pessoa):
    def __init__(self, nome, nasc, salario):
        super().__init__(nome, nasc)
        self._salario = salario

    def __repr__(self):
        return f"Professor de nome {self._nome}, data de nascimento {self._nasc}, que recebe um salario de {self._salario} reais."


x = Pessoa("Maria", "01/03/1992")
y = Estudante("José", "02/07/1987", "Medicina")
z = Professor("João", "03/09/1965", 10000.0)

print(x)
print(y)
print(z)
