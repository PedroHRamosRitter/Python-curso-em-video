class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)

    def get_nota(self): # Metódo Getter
        return self._nota

    def set_nota(self, valor): # Metódo Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print(f"Nota inválida")

