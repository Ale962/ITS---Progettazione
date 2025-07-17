from asta import *
from bid import *

class asta_bid:

    class _link:

        _asta: Asta # immutabile
        _bid: Bid # immutabile, non noto alla nascita

        def __init__(self, asta: Asta, bid: Bid):
            self._asta = asta
            self._bid = bid

        def get_asta(self) -> Asta:
            return self._asta
        
        def get_bid(self) -> Bid:
            return self._bid
        
        def __repr__(self):
            return f'Bid: {self.get_bid().__repr__()}, Asta: {self.get_asta().__repr__()}'