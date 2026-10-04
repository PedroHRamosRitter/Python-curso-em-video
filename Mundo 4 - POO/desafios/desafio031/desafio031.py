class Retangulo:
    def __init__(self, base = 1, altura = 1):

        # Atributos da instância
        self._base = None
        self._altura = None
        self._area = None

        # Atributos dos property para assim dizer
        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError(f"O valor da base deve ser um número")
        if valor < 0:
            raise ValueError(f"Valor inválido para a base")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError(f"O valor da altura deve ser um número")
        if valor < 0:
            raise ValueError(f"Valor inválido para a Altura")
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError(f"Área não pode ser definida desse jeito")

    @property
    def medidas(self):
            return f"Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}"

    @medidas.setter
    def medidas(self, valor:list):
        if not isinstance(valor, list):
            raise TypeError(f"As medidas devem ser informadas dentro de uma lista")
        if len(valor) != 2:
            raise SyntaxError(f"Informe uma lista com apenas dois valores numéricos")
        if isinstance(valor[0], float) or isinstance(valor[0], int):
            self._base = valor[0]
        else:
            raise TypeError(f"A base deve ser um número")
        if isinstance(valor[1], float) or isinstance(valor[1], int):
            self._altura = valor[1]
        else:
            raise TypeError(f"A altura deve ser um número")
