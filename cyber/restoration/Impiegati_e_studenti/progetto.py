from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from impiegato import Impiegato
from res_prog import res_prog

class Progetto:

    _nome: str # Immutabile, noto alla nascita
    _impiegati: set[tuple[res_prog._link, 'Impiegato']]

    def __init__(self, nome: str):
        self._nome = nome
        self._impiegati = set()

    def nome(self) -> str:
        return self._nome
    
    def impiegati(self) -> frozenset[res_prog._link, 'Impiegato']:
        return frozenset(self._impiegati)

    def add_impiegato(self, l: res_prog._link, impiegato: 'Impiegato') -> None:
        for t in self._impiegati:
            x,y = t
            if y == impiegato:
                raise ValueError(f"L'impiegato {impiegato} è già presente")
        else:
            tu = (l, impiegato)
            self._impiegati.add(tu)

    def remove_impiegato(self, l: res_prog._link)-> None:
        for t in self._impiegati:
            x,y = t
            if y == l.impiegato():
                self._impiegati.remove(t)
                break
            else:
                raise RuntimeError(f'{l.impiegato()} non presente')

    def impiegati(self) -> frozenset[tuple[res_prog._link, 'Impiegato']]:
        return frozenset(self._impiegati)
    
    def __repr__(self):
        return f'{self.nome()}'