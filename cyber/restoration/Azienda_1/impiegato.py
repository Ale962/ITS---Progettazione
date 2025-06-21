from datetime import date
from custom_types import RealGEZ

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from progetto import Progetto

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGEZ # noto alla nascita
    _progetti: set['Progetto'] | None # non necessariamente noto alla nascita


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._progetti: set[Progetto] = set()

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s

    def add_progetto(self, p: 'Progetto') -> None:
        if p not in self._progetti:
            self._progetti.add(p)
            try:
                p.add_impiegato(self)
            except ValueError:
                pass
        else:
            ValueError('Progetto già presente')

    def remove_progetto(self, p: 'Progetto') -> None:
        try:
            self._progetti.remove(p)
            try:
                p.remove_impiegato(self)
            except ValueError:
                pass
        except IndexError:
            pass

    def progetti(self) -> frozenset['Progetto']:
        return frozenset(self._progetti)
    

    def __repr__(self) -> str:
        return f"Impiegato {self.nome()}, {self.cognome()}"