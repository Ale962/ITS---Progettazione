from __future__ import annotations
from typing import Self, Type
from typing import Any
import re
from datetime import date
from enum import *


class RealGEZ(float):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")

class IntGEZ(int):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: int = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")


class Telefono(str):
    def __new__(cls, t: str | Self) -> Self:
        if re.fullmatch(r"^\d{10}$", t):
            return super().__new__(cls, t)
        raise ValueError(f"'{t}' non è un numero di telefono italiano valido")


class CAP(str):
    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^\d{5}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")


class CodiceFiscale(str):
    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^[A-Z0-9]{16}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un Codice Fiscale italiano valido!")

class Indirizzo:
    # campi dati:
    _via:str
    _civico: str
    _cap: CAP
    def __init__(self, via: str, civico: str, cap: CAP) -> None:
        self._via: str = via

        if not re.search("^[0-9]+[a-zA-Z]*$", civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico: str = civico
        self._cap: CAP = cap

    def via(self) -> str:
        return self._via

    def civico(self) -> str:
        return self._civico

    def cap(self) -> str:
        return self._cap

    def __repr__(self) -> str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()}, cap={self.cap()})"

    def __str__(self) -> str:
        return f"{self.via()} {self.civico()} - {self.cap()}"

    # class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
    def __hash__(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())

class Genere(StrEnum):
    uomo = auto()
    donna = auto()

class Ruolo(StrEnum):
    segretario = auto()
    direttore = auto()
    progettista = auto()

class PosizioneMilitare(StrEnum):

    Soldato = auto()
    Caporale = auto()
    Caporale_Maggiore = auto()
    Graduato = auto()
    Graduato_Scelto = auto()
    Graduato_Capo = auto()
    Primo_Graduato = auto()
    Graduato_Aiutante = auto() 
    Sergente = auto()
    Sergente_Maggiore = auto()
    Sergente_Maggiore_Capo = auto()
    Sergente_Maggiore_Aiutante = auto()
    Maresciallo = auto()
    Maresciallo_Ordinario = auto()
    Maresciallo_Capo = auto()
    Primo_Maresciallo = auto()
    Luogotenente = auto()
    Primo_Luogotenente = auto()
    Sottotenente = auto()
    Tenente = auto()
    Capitano = auto()
    Maggiore = auto()
    Tenente_Colonnello = auto()
    Colonnello = auto()
    Generale_di_Brigata = auto()
    Generale_di_Divisione = auto()
    Generale_di_Corpo_di_Armata = auto()

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
    
class Studente(Persona):

    _matricola: int # Immutabile, noto alla nascita

    def __init__(self, nome, cognome, cf, nascita, genere, matricola: int, maternita = None, posizione_militare = None):
        super().__init__(nome, cognome, cf, nascita, genere, maternita, posizione_militare)
        self._matricola = matricola

    def matricola(self) -> int:
        return self._matricola
    
    def __repr__(self):
        return super().__repr__()+f' matricola: {self.matricola()}'
    
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
    
class res_prog:

    res_prog_link: dict[res_prog._link, dict[str, Impiegato|Progetto]] = {}

    @classmethod
    def add_link(cls, i: Impiegato, p: Progetto):
        l: __class__._link = __class__._link(i, p)
        __class__.res_prog_link[l] = {'Impiegato': i, 'Progetto': p}
        i.add_progetto(l, p)
        p.add_impiegato(l, i)

    @classmethod
    def remove_link(cls, l: res_prog._link):
        if l in __class__.res_prog_link:
            l.impiegato().remove_progetto(l)
            l.progetto().remove_impiegato(l)
            del __class__.res_prog_link[l]

    @classmethod
    def get_res_prog_link(cls) -> frozenset[dict[res_prog._link, dict[str, Impiegato|Progetto]]]:
        return frozenset(cls.res_prog_link)
        
    class _link:

        _impiegato: Impiegato # immutabile, noto alla nascita
        _progetto: Progetto # immutabile, noto alla nascita

        def __init__(self, i: Impiegato, p: Progetto):
            self._impiegato = i
            self._progetto = p

        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def progetto(self) -> Progetto:
            return self._progetto
        
        def __repr__(self):
            return f'Il responsabile {self.impiegato()} si occupa del progetto {self.progetto()}'