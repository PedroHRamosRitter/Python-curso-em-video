class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)

    # Criando Atributo Validável

    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter # Setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print(f"Nota inválida!")

    @nota.deleter
    def nota(self):
        pass