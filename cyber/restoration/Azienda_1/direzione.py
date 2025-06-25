from __future__ import annotations
from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any

class direzione:

    direnzione_link: list[dict[Impiegato, list[Dipartimento], list[_link]]]

    @classmethod
    def add_link(cls, dipartimento: Dipartimento, impiegato: Impiegato):
        for x in cls.direnzione_link:
                for y in x.get('Dipartimenti'):
                    if y == dipartimento:
                        raise ValueError('Dipartimento già diretto')
                
        found: bool = False
        for x in cls.direnzione_link:
            for y in x.get('Impiegato'):
                if y == impiegato:
                    l: __class__._link = __class__._link(impiegato, dipartimento)
                    ['Dipartimenti'].append({'Dipartimento': dipartimento})
                    ['Link'].append(l)
                found = True
        if not found:
            l: __class__._link = __class__._link(impiegato, dipartimento)
            di = {'Dipartimento': dipartimento}
            d = {'Impiegato': impiegato, 'Dipartimento': [di], 'Link': [l]}
            cls.direnzione_link.append(d)

    @classmethod
    def remove_link(cls, link: _link):
        if link:
            for x in cls.direnzione_link:
                for y in x.get('Link'):
                    if y == link:
                        if not x.get('Dipartimenti'):
                            cls.direnzione_link.pop(x)
                        else:
                            x.get('Dipartimenti').pop(link.impiegato())        
                            x.get('Link').pop(link)


    class _link:
        _impiegato: Impiegato # immutabile noto alla nascita
        _dipartimento: Dipartimento # immutabile noto alla nascita

        def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento):
            self._impiegato: Impiegato = impiegato
            self._dipartimento: Dipartimento = dipartimento
        
        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def dipartimento(self) -> Dipartimento:
            return self._dipartimento
        
        def __hash__(self) -> int:
                return hash((self.impiegato(), self.dipartimento()))
            
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                    return False
                
            return (self.impiegato(), self.dipartimento()) == (other.impiegato(), other.dipartimento())