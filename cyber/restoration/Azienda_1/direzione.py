from custom_types import *
from dipartimento import *
from impiegato import *
from typing import Any

class direzione:

    class _link:
        _impiegato: Impiegato # immutabile noto alla nascita
        _dipartimento: Dipartimento # immutabile noto alla nascita

        def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento):
            self._impiegato: Impiegato = impiegato
            self._dipartimento: Dipartimento = dipartimento
        
        def impiegato(self) -> Impiegato:
            return self._impiegato
        
        def dipartimento(self) -> Dipartimento:
            return self._dipartimento
        
        def __hash__(self) -> int:
                return hash((self.impiegato(), self.dipartimento()))
            
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                    return False
                
            return (self.impiegato(), self.dipartimento()) == (other.impiegato(), other.dipartimento())