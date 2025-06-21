from custom_types import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from impiegato import Impiegato

class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita
    _impiegati: set['Impiegato']# non noto alla nascita

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati: set['Impiegato'] = set()

    def set_nome(self, nome:str) -> None:
        self._nome = nome 

    def set_budget(self, budget: RealGEZ) -> None:
        self._budget = budget

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def add_impiegato(self, impiegato: 'Impiegato') -> None:
        if impiegato not in self._impiegati:
            self._impiegati.add(impiegato)
            impiegato.add_progetto(self)
        else:
            raise ValueError(f'{impiegato} già presente')

    def remove_impiegato(self, impiegato: 'Impiegato') -> None:
        try:
            self._impiegati.remove(impiegato)
            if impiegato in self._impiegati:
                impiegato.remove_progetto(self)
            else: 
                raise ValueError (f"L' {impiegato} non è presente!")
        except IndexError:
            pass

    def impiegati(self) -> frozenset['Impiegato']:
        return frozenset(self._impiegati)
    
    def __repr__(self) -> str:
        return f"Progetto {self.nome()}"
