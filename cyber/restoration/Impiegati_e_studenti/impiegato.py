from custom_types import *
from persona import Persona

class Impiegato(Persona):

    _stipendio: RealGEZ # noto alla nascita
    _ruolo: Ruolo # noto alla nascita
    _is_responsabile: bool # noto alla nascita

    def __init__(self, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool, nome, cognome, cf, nascita, genere, maternita = None, posizione_militare = None):
        super().__init__(nome, cognome, cf, nascita, genere, maternita, posizione_militare)
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        self.set_is_responsabile(is_responsabile)

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
    
    def __repr__(self):
        return super().__repr__()+f' {self.stipendio()} {self.ruolo()}'