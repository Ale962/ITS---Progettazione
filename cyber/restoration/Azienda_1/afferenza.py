from __future__ import annotations
from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any
from datetime import datetime

class afferenza:

    afferenza_link: dict[ _link, dict[Dipartimento, list[dict[Impiegato, datetime]]]] = {}

    @classmethod
    def add_link(cls, dipartimento: Dipartimento, impiegato: Impiegato, data_afferenza: datetime):
        for x in list(cls.afferenza_link):
            for i in cls.afferenza_link[x]['Impiegati']:
                if i['Impiegato'] == impiegato:
                    raise ValueError('Impiegato già presente in un altro Dipartimento')
                
        found: bool = False
        for x in list(cls.afferenza_link):
            if cls.afferenza_link[x]['Dipartimento'] == dipartimento:
                d = cls.afferenza_link[x]
                d['Impiegati'].append({'Impiegato': impiegato, 'Data afferenza': data_afferenza})
                found = True
        if not found:
            l: __class__._link = __class__._link(impiegato, dipartimento, data_afferenza)
            cls.afferenza_link[l] = {'Dipartimento': dipartimento, 'Impiegati': [{'Impiegato': impiegato, 'Data afferenza': data_afferenza}]}

    @classmethod
    def remove_link(cls, link: _link|None = None, dipartimento: Dipartimento|None = None, impiegato: Impiegato|None = None):
        if link in cls.afferenza_link:
                cls.afferenza_link.pop(link)

        if impiegato:
            for x in list(cls.afferenza_link):
                for i in cls.afferenza_link[x]['Impiegati']:
                    if i['Impiegato'] == impiegato:
                        cls.afferenza_link[x]['Impiegati'].remove(i)
                        break

        if dipartimento:
            for x in list(cls.afferenza_link):
                if cls.afferenza_link[x]['Dipartimento'] == dipartimento:
                    cls.afferenza_link.pop(x)

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