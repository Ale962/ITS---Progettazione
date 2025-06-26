from persona import Persona
from custom_types import *

class Studente(Persona):

    _matricola: int # Immutabile, noto alla nascita

    def __init__(self, nome, cognome, cf, nascita, genere, matricola: int, maternita = None, posizione_militare = None):
        super().__init__(nome, cognome, cf, nascita, genere, maternita, posizione_militare)
        self._matricola = matricola

    def matricola(self) -> int:
        return self._matricola
    
    def __repr__(self):
        return super().__repr__()+f' matricola: {self.matricola()}'