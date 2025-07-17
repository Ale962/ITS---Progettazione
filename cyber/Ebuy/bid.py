from datetime import *
from bid_ut import bid_ut
from asta_bid import asta_bid
from privato import Privato
from asta import Asta
from typing import Self

class Bid:

    _istante: datetime # immutabile
    _link_utente: bid_ut._link
    _link_asta: asta_bid._link
    
    def __init__(self, istante: datetime, utente: Privato, asta: Asta):
        self._istante = istante
        self.__add_link_utente(utente, self)
        self.__add_link_asta(asta, self)

    def get_istante(self) -> datetime:
        return self._istante
    
    def __add_link_utente(self, u: Privato) -> None:
        l = bid_ut._link(u, self)
        self._link_utente = l
        l.get_privato().add_bid(l)

    def __add_link_asta(self, a: Asta) -> None:
        l = asta_bid._link(a, self)
        self._link_asta = l
        l.get_asta().add_bid(l)
    
    def get_privato(self):
        self._link_utente.get_privato()
    
    def get_asta(self):
        self._link_asta.get_asta()


    def __repr__(self):
        return f"{self.get_privato().__repr__()} fa bid in asta {self.get_asta().__repr__()} all'istante {self.get_istante()}"