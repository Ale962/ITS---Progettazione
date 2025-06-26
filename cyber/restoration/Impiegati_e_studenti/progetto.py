class Progetto:

    _nome: str # Immutabile, noto alla nascita

    def __init__(self, nome: str):
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def __repr__(self):
        return f'{self.nome()}'