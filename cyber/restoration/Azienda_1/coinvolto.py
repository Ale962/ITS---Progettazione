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
    def remove_link(cls, link: _link|None = None, impiegato: Impiegato|None = None, progetto: Progetto|None = None):

        if link:
            for x in cls.coinvolto_link and cls.coinvolto_link():
                cls.coinvolto_link.pop(link)

        if impiegato:
            for x in list(cls.coinvolto_link):
                if cls.coinvolto_link[x]['Impiegato'] == impiegato:
                    cls.coinvolto_link.pop(impiegato)

        if progetto:
            for x in list(cls.coinvolto_link):
                if cls.coinvolto_link[x]['Progetto'] == progetto:
                    cls.coinvolto_link.pop(progetto)

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