from Volo import Volo
from Aereoporto import Aereoporto
from typing import Any

class arrivo:
    class _link:
        _volo: set[Volo] # non necessariamente noto alla nascità
        _aereoporto: Aereoporto # sempre immutabile, noto alla nascità

        def aereoporto(self) -> Aereoporto:
            return self._aereoporto
        
        def volo(self) -> frozenset[Volo]:
            return self._volo
        
        def __init__(self,a: Aereoporto, v: Volo = None):
            self._aereoporto: Aereoporto = a
            self._volo: set[Volo] = {}
            if v:
                self.add_volo(v)

        def add_volo(self, v: Volo) -> None:
            self._volo.add(v)

        def remove_volo(self, v: Volo) -> None:
            self._volo.remove(v)
            if not self._volo:
                return None
            
        def __hash__(self) -> int:
            return hash((self.aereoporto(), self.volo()))
        
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.aereoporto(), self.volo()) == (other.aereoporto(), other.volo())