class Endereco:
    def __init__(self, num, rua, cidade, estado, cep, apt=""):
        self.num = num  # str
        self.rua = rua  # str
        self.cidade = cidade  # str
        self.estado = estado  # str
        self.cep = cep  # str (XXXXX-XXX)
        self.apt = apt  # str

    def imprimir(self):
        print(self.rua, end="")
        print(",", self.num)
        print(self.cidade, end="")
        print(",", self.estado, end="")
        print(",", self.cep)

    def mesmo_setor(self, outro):
        return self.cep[:3] == outro.cep[:3]


# end1 = Endereco("10", "Rua Sem Nome", "Penedo", "Alagoas", "55566-777")
# end2 = Endereco("20", "Rua Aleatória", "Penedo", "Alagoas", "55566-777")
# end1.imprimir()
# end2.imprimir()
# print(end1.mesmo_setor(end2))
