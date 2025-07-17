from utente import *
from bid import Bid
from bid_ut import bid_ut

class Privato(Utente):
    _bids: dict[Bid, bid_ut._link]

    def __init__(self, username, registrazione):
        super().__init__(username, registrazione)
        self._bids: dict[Bid, bid_ut._link] = {}

    def get_bids(self) -> frozenset[dict[Bid, bid_ut._link]]:
        return frozenset(self._bids)
    
    def add_bid(self, b: bid_ut._link):
        self._bids[b.get_bid()] = [b]

    def __repr__(self):
        return super().__repr__()