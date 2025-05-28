from Compagnia_Aerea import Compagnia_Area
from Volo import Volo
from typing import Any

class responsabile:
    class _link:
        _compagnia: Compagnia_Area # sempre immutabile, noto alla nascità
        _volo: Volo # non necessariamente noto alla nascità

        def compagnia(self) -> Compagnia_Area:
            return self._compagnia
        
        def volo(self) -> frozenset[Volo] | None:
            return self._volo
        
        def __init__(self, c: Compagnia_Area, v: set[Volo] = None):
            self._compagnia: Compagnia_Area = c
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
            return hash((self.compagnia(), self.volo()))
        
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.compagnia(), self.volo()) == (other.compagnia(), other.volo())