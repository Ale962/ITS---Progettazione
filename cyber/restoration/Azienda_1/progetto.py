from custom_types import *

class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)

    def set_nome(self, nome:str) -> None:
        self._nome = nome 

    def set_budget(self, budget: RealGEZ) -> None:
        self._budget = budget

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def __repr__(self) -> str:
        return f"Progetto {self.nome()} con budget {self.budget()}"