from __future__ import annotations
from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any
from datetime import datetime

class afferenza:

    afferenza_link: list[dict[str, Dipartimento | list[dict[str, Impiegato | datetime]] | list[afferenza._link]]] = []

    @classmethod
    def add_link(cls, dipartimento: Dipartimento, impiegato: Impiegato, data_afferenza: datetime):
        for x in cls.afferenza_link:
                for y in x.get('Impiegati'):
                    if y == impiegato:
                        raise ValueError('Impiegato già assegnato')
                
        found: bool = False
        for x in cls.afferenza_link:
            if x.get('Dipartimento') == dipartimento:
                l: __class__._link = __class__._link(impiegato, dipartimento, data_afferenza)
                i: dict[str, Impiegato | datetime] = {'Impiegato': impiegato, 'Data Afferenza': data_afferenza}
                x['Impiegati'].append(i)
                x['Link'].append(l)
                found = True
        if not found:
            l: __class__._link = __class__._link(impiegato, dipartimento, data_afferenza)
            d = {'Dipartimento': dipartimento, 'Impiegati': [{'Impiegato': impiegato, 'Data Afferenza': data_afferenza}], 'Link': [l]}
            cls.afferenza_link.append(d)

    @classmethod
    def remove_link(cls, link: _link):
        
        for x in cls.afferenza_link:
            y = x.get('Link')
            for l in y:
                if l == link:
                    imp = x.get('Impiegati')
                    imp[:] = [i for i in imp if i.get('Impiegato') != link.impiegato()]
                    if link in y:
                        y.remove(link)
                    if not imp:
                        cls.afferenza_link.remove(x)

    class _link:
        _impiegato: Impiegato # immutabile noto alla nascita
        _dipartimento: Dipartimento # immutabile noto alla nascita
        _data_afferenza: datetime # Immutabile noto alla nascita

        def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento, data_afferenza: datetime):
            self._impiegato: Impiegato = impiegato
            self._dipartimento: Dipartimento = dipartimento
            self._data_afferenza: datetime = data_afferenza

        def data_afferenza(self) -> datetime:
            return self._data_afferenza
        
        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def dipartimento(self) -> Dipartimento:
            return self._dipartimento
        
        def __hash__(self) -> int:
                return hash((self.impiegato(), self.dipartimento(), self.data_afferenza()))
            
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                    return False
                
            return (self.impiegato(), self.dipartimento(), self.data_afferenza()) == (other.impiegato(), other.dipartimento(), other.data_afferenza())
        
        def __repr__(self):
            return f"L'impiegato {self.impiegato().nome()} {self.impiegato().cognome()} afferisce al dipartimento {self.dipartimento().nome()} dal {self.data_afferenza()}"