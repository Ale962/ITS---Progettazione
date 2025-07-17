from __future__ import annotations
from custom_types import *
from datetime import datetime

class Utente:
    _username: str # immutabile
    _registrazione: datetime # immutabile

    def __init__(self,username: str, registrazione: datetime):
        self._username = username
        self._registrazione = registrazione
    
    def get_username(self) -> str:
        return self._username
    
    def get_registrazione(self) -> datetime:
        return self._registrazione

    def __repr__(self):
        return f'Username: {self.get_username()}, iscritto: {self.get_registrazione()}'
    
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
    
class VenditoreProf(Utente):
    _vetrina: URL

    def __init__(self, username, registrazione, vetrina: URL):
        super().__init__(username, registrazione)
        self.set_vetrina(vetrina)

    def set_vetrina(self, vetrina) -> None:
        self._vetrina = vetrina
    
    def get_vetrina(self) -> URL:
        return self._vetrina
    
    def __repr__(self):
        return super().__repr__() + f'link vetrina: {self.get_vetrina()}'
    
class PostOggetto:

    _prezzo: RealGEZ
    _anni_garanzia: IntGEZ
    _descrizione: str
    _pubblicazione: datetime # immutabile
    _is_nuovo: bool # immutabile
    _condizione: Condizione|None # immutabile

    def __init__(self, prezzo: RealGEZ, anni_garanzia: IntGEZ, descrizione: str, pubblicazione: datetime, _is_nuovo: bool = False, condizione: Condizione|None = None):
        self.set_prezzo(prezzo)
        self.set_anni_garanzia(anni_garanzia)
        self.set_descrizione(descrizione)
        self._pubblicazione = pubblicazione
        if _is_nuovo:
            self._is_nuovo = _is_nuovo
        if condizione:
            self._condizione = condizione

    def set_prezzo(self, prezzo: RealGEZ) -> None:
        self._prezzo = prezzo
    
    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self._anni_garanzia = anni_garanzia

    def set_descrizione(self, descrizione: str) -> None:
        self._descrizione = descrizione

    def get_prezzo(self) -> RealGEZ:
        return self._prezzo
    
    def get_anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def get_descrizione(self) -> str:
        return self._descrizione
    
    def get_pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def get_is_nuovo(self) -> bool:
        if self._is_nuovo:
            return self._is_nuovo
    
    def get_condizione(self) -> Condizione:
        if self._condizione != None:
            return self._condizione
        
    def __repr__(self):
        if self._is_nuovo:
            return f'{self.get_descrizione()}\nPrezzo: {self.get_prezzo()}\nAnni garanzia: {self.get_anni_garanzia()}\nData pubblicazione: {self.get_pubblicazione()}'
        
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