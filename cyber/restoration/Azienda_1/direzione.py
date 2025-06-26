from __future__ import annotations
from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any

class direzione:

    direnzione_link: list[dict[str, Impiegato | list[Dipartimento] | list[direzione._link]]] = []

    @classmethod
    def add_link(cls, dipartimento: Dipartimento, impiegato: Impiegato):
        for x in cls.direnzione_link:
                for y in x.get('Dipartimenti'):
                    if y == dipartimento:
                        raise ValueError('Dipartimento già diretto')
                
        found: bool = False
        for x in cls.direnzione_link:
            if x.get('Impiegato') == impiegato:
                l: __class__._link = __class__._link(impiegato, dipartimento)
                x['Dipartimenti'].append(dipartimento)
                x['Link'].append(l)
                found = True
        if not found:
            l: __class__._link = __class__._link(impiegato, dipartimento)
            d = {'Impiegato': impiegato, 'Dipartimenti': [dipartimento], 'Link': [l]}
            cls.direnzione_link.append(d)

    @classmethod
    def remove_link(cls, link: _link):
        if link:
            for x in cls.direnzione_link:
                y = x.get('Link')
                for l in y:
                    if l == link:
                        dip = x.get('Dipartimenti')
                        dip [:] = [d for d in dip if d != link.dipartimento()]
                        # if link.dipartimento() in dip:
                        #    dip.remove(link.dipartimento())
                        if link in y:
                            y.remove(link)
                        if not dip:
                            cls.direnzione_link.remove(x)
                        
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
        
        def __repr__(self):
            return f"L'impieagto {self.impiegato().nome()} {self.impiegato().cognome()} dirige il dipartimento {self.dipartimento().nome()}"