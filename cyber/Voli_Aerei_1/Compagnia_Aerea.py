from datetime import datetime, date
from Città import Città

class Compagnia_Area:
    _name : str # noto alla nascita
    _fondazione : date # immutabile, noto alla nascita
    _sede : Città # può essere non noto alla nascità

    def name(self) -> str:
        return self._name
    
    def fondazione(self) -> date:
        return self._fondazione
    
    def sede(self) -> Città:
        return self._sede
    
    def set_name(self, n: str) -> None:
        self._name = n

    def set_sede(self, c: Città | None) -> None:
        self._sede = c

    def __init__(self, name: str, fondazione: date, sede: Città = None):
        
        self.set_name(name)
        self.set_sede(sede)
        self._fondazione = fondazione