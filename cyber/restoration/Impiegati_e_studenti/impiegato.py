from custom_types import *
from persona import Persona
from progetto import Progetto
from res_prog import res_prog

class Impiegato(Persona):

    _stipendio: RealGEZ # noto alla nascita
    _ruolo: Ruolo # noto alla nascita
    _is_responsabile: bool # noto alla nascita
    _progetti: set[tuple[res_prog._link, Progetto]]

    def __init__(self, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool, nome, cognome, cf, nascita, genere, maternita = None, posizione_militare = None):
        super().__init__(nome, cognome, cf, nascita, genere, maternita, posizione_militare)
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        self.set_is_responsabile(is_responsabile)
        self._progetti = set()

    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s

    def set_ruolo(self, r: Ruolo) -> None:
        self._ruolo = r

    def set_is_responsabile(self, ir: bool) -> None:
        self._is_responsabile = ir

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def is_responsabile(self) -> bool:
        return self._is_responsabile
    
    def add_progetto(self, l: res_prog._link, progetto: Progetto) -> None:
        if self.is_responsabile():    
            for t in self._progetti:
                x,y = t
                if y == progetto:
                    raise ValueError(f"Il progetto {progetto} è già presente")
            else:
                tu = (l, progetto)
                self._progetti.add(tu)

    def remove_progetto(self, l: res_prog._link)-> None:
        for t in self._progetti:
            x,y = t
            if y == l.progetto():
                self._progetti.remove(t)
                break
            else:
                raise RuntimeError(f'{l.progetto()} non presente')

    def progetti(self) -> frozenset[tuple[res_prog._link, Progetto]]:
        return frozenset(self._progetti)
    
    def __repr__(self):
        return super().__repr__()+f' stipendio: {self.stipendio()}, ruolo: {self.ruolo()}'