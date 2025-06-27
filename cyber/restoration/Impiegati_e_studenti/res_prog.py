from __future__ import annotations
from impiegato import *
from progetto import *

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