from custom_types import *
from datetime import datetime

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