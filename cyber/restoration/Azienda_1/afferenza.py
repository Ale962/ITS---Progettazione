from __future__ import annotations
from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any
from datetime import datetime

class afferenza:

    afferenza_link: list[dict[Dipartimento, list[Impiegato, datetime], list[_link]]] = {}

    @classmethod
    def add_link(cls, dipartimento: Dipartimento, impiegato: Impiegato, data_afferenza: datetime):
        for x in cls.afferenza_link:
                for y in x.get('Impiegati'):
                    if y == impiegato:
                        raise ValueError('Impiegato già presente in un altro Dipartimento')
                
        found: bool = False
        for x in cls.afferenza_link:
            for y in x.get('Dipartimento'):
                if y == dipartimento:
                    l: __class__._link = __class__._link(impiegato, dipartimento, data_afferenza)
                    ['Impiegati'].append({'Impiegato': impiegato, 'Data afferenza': data_afferenza})
                    ['Link'].append(l)
                found = True
        if not found:
            l: __class__._link = __class__._link(impiegato, dipartimento, data_afferenza)
            i = {'Impiegato': impiegato, 'Data Afferenza': data_afferenza}
            d = {'Dipartimento': dipartimento, 'Impiegati': i, 'Link': [l]}
            cls.afferenza_link.append(d)

    @classmethod
    def remove_link(cls, link: _link):
        if link:
            for x in cls.afferenza_link:
                for y in x.get('Link'):
                    if y == link:
                        if not x.get('Impiegati'):
                            cls.afferenza_link.pop(x)
                        else:
                            x.get('Impiegati').pop(link.impiegato())        
                            x.get('Link').pop(link)
                        
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