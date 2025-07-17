from privato import *
from bid import *

class bid_ut:
        
    class _link:
        _privato: Privato # immutabili
        _bid: Bid # immutabili, non noto alla nascita

        def __init__(self, privato: Privato, bid: Bid):
            self._privato = privato
            self._bid = bid

        def get_privato(self) -> Privato:
            return self._privato
        
        def get_bid(self) -> Bid:
            return self._bid
        
        def __repr__(self):
            return f'Utente: {self.get_privato().__repr__()}, bid: {self.get_bid().__repr__()}'