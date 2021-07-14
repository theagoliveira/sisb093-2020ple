class Calcado:
    # VARIÁVEIS DE CLASSE
    tamanho_max = 44
    tamanho_min = 36

    def __init__(self, tamanho, material, preco, emPromocao=False):
        # VARIÁVEIS DE INSTÂNCIA
        self._tamanho = tamanho
        self._material = material
        self._preco = preco
        self._emPromocao = emPromocao

    # MÉTODOS

    # REPRESENTAÇÃO EM FORMATO STRING
    def __repr__(self):
        return f"Calçado de tamanho {self._tamanho} feito em {self._material} que custa {self._preco} reais."

    def get_tamanho(self):
        return self._tamanho

    # def get_material(self):
    #    return self._material

    def get_emPromocao(self):
        return self._emPromocao

    def set_emPromocao(self, v):
        self._emPromocao = v

    # OPERADOR +
    def __add__(self, outro):
        return self._preco + outro._preco

    # OPERADOR ==
    def __eq__(self, outro):
        return (
            (self._tamanho == outro._tamanho)
            and (self._material == outro._material)
            and (self._preco == outro._preco)
        )

    # OPERADOR !=
    def __ne__(self, outro):
        return not (self == outro)


class Sandalia(Calcado):
    def __init__(self, marca, tamanho, material, preco, emPromocao=False):
        # INICIALIZAR ATRIBUTOS DA SUPERCASSE
        super().__init__(tamanho, material, preco, emPromocao)
        # INICIALIZAR NOVOS ATRIBUTOS
        self._marca = marca

    # REDEFINIR MÉTODO DA SUPERCLASSE
    def __repr__(self):
        return f"Sandália da marca {self._marca} de tamanho {self._tamanho} feito em {self._material} que custa {self._preco} reais."

    # DEFINIR NOVOS MÉTODOS
    def get_marca(self):
        return self._marca
