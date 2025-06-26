from __future__ import annotations
from custom_types import *
from progetto import *
from impiegato import *
from typing import Any

class coinvolto:

    coinvolto_link: dict[_link, dict[Impiegato, Progetto]] = {}

    @classmethod
    def add_link(cls, impiegato: Impiegato, progetto: Progetto):
        l: __class__._link = __class__._link(impiegato, progetto)
        cls.coinvolto_link[l] = {'Impiegato': impiegato, 'Progetto': progetto}
        
    @classmethod
    def remove_link(cls, link: coinvolto._link):
        if link in cls.coinvolto_link:
            del cls.coinvolto_link[link]

    class _link:
        _impiegato: Impiegato # sempre immutabile e noto alla nascita
        _progetto: Progetto # sempre immutabile e noto alla nascita

        def __init__(self, impiegato: Impiegato, progetto: Progetto):
            self._impiegato: Impiegato = impiegato
            self._progetto: Progetto = progetto

        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def progetto(self) -> Progetto:
            return self._progetto
        
        def __hash__(self) -> int:
                return hash((self.impiegato(), self.progetto()))
            
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                    return False
                
            return (self.impiegato(), self.progetto()) == (other.impiegato(), other.progetto())
        
        def __repr__(self):
            return f"{self.impiegato()} è coinvolto nei seguenti progetti {self.progetto()}"