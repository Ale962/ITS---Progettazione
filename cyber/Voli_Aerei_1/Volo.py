from My_Types import IntGZ
from datetime import time

class Volo:
    _codice: IntGZ # Immutabile, noto alla nascità
    _durata: time # Immutabile, noto alla nascità

    def codice(self) -> IntGZ:
        return self._codice
    
    def durata(self) -> time:
        return self._durata
    
    def __init__(self, codice: IntGZ, durata: time):
        
        self._codice = codice
        self._durata = durata