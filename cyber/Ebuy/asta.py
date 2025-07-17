from postoggetto import *
from bid import Bid
from asta_bid import asta_bid

class Asta(PostOggetto):
    _prezzo_bid: RealGEZ
    _scadenza: datetime
    _bids: dict[Bid, asta_bid._link]

    def __init__(self, prezzo_bid: RealGEZ, scadenza: datetime, prezzo, anni_garanzia, descrizione, pubblicazione, _is_nuovo = False, condizione = None):
        super().__init__(prezzo, anni_garanzia, descrizione, pubblicazione, _is_nuovo, condizione)
        self.set_prezzo_bid(prezzo_bid)
        self.set_scadenza(scadenza)
        self._bids: set[dict[Bid, asta_bid._link]] = ()
    
    def set_prezzo_bid(self, prezzo_bid: RealGEZ) -> None:
        self._prezzo_bid = prezzo_bid

    def set_scadenza(self, scadenza: datetime) -> None:
        self._scadenza = scadenza

    def get_prezzo_bid(self) -> RealGEZ:
        return self._prezzo_bid
    
    def get_scadenza(self) -> datetime:
        return self._scadenza
    
    def get_bids(self) -> frozenset[dict[Bid, asta_bid._link]]:
        return frozenset(self._bids)
    
    def add_bid(self, b: asta_bid._link):
        self._bids[b.get_bid()] = [b]
         
    def __repr__(self):
        return super().__repr__() + f'\nUltimo prezzo bid: {self.get_prezzo_bid()}\nScadenza asta: {self.get_scadenza()}'