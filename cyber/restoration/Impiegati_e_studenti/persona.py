from custom_types import *
from datetime import date
from posizione_militare import PosizioneMilitare

class Persona:

    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _cf: set[CodiceFiscale] # noto alla nascita
    _nascita: date # immutabile, noto alla nascita
    _genere: Genere # noto alla nascita
    _maternita: IntGEZ | None # noto alla nascita
    _posizione_militare: PosizioneMilitare # noto alla nascita

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, genere: Genere, maternita: IntGEZ|None = None, posizione_militare: PosizioneMilitare|None = None):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._cf = set()
        self.add_codice_fiscale(cf)
        self._nascita = nascita
        self.set_genere(genere)
        if self.genere() == 'donna':
            if not maternita:
                raise ValueError('Le donne devono avere per forza avere un numero di maternita')
            self.set_maternita(maternita)
        else:
            if not posizione_militare:
                raise ValueError('Gli uomini devono avere per forza avere una posizione militare')
            self.set_posizione_militare(posizione_militare)

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_genere(self, g: Genere) -> None:
        self._genere = g
    
    def set_maternita(self, n: IntGEZ) -> None:
        self._maternita = n

    def set_posizione_militare(self, p:PosizioneMilitare):
        self._posizione_militare = p

    def add_codice_fiscale(self, cf: CodiceFiscale) -> None:
        self._cf.add(cf)

    def remove_codice_fiscale(self, cf: CodiceFiscale) -> None:
        self._cf.remove(cf)

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def codice_fiscale(self) -> frozenset[CodiceFiscale]:
        return frozenset(self._cf)
    
    def nascita(self) -> date:
        return self._nascita
    
    def genere(self) -> Genere:
        return self._genere
    
    def maternita(self) -> int:
        if not self.genere() == 'donna':
            raise RuntimeError('Questa persona non è una donna non ha un numero di maternita definito')
        else:
            return self._maternita
        
    def posizione_militare(self) -> PosizioneMilitare:
        if not self.genere() == 'uomo':
            raise RuntimeError('Questa persona non è un uomo non ha una posizione militare definita')
        else:
            return self._posizione_militare
        
    def __repr__(self):
        return f'{self.nome()} {self.cognome()} {self.codice_fiscale()} {self.nascita()} {self.genere()}'