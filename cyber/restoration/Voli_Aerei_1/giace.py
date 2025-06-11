from Aereoporto import Aereoporto
from Città import Città
from typing import Any

class giace:
    class _link:
        _città: Città # noto alla nascità
        _aereoporto: set[Aereoporto] # non noto alla nascità

        def città(self) -> Città:
            return self._città
        
        def aereoporto(self) -> Aereoporto:
            return self._aereoporto
        
        def __init__(self, c: Città, a: Aereoporto = None):
            self._città = c
            self._aereoporto: set[Aereoporto] = {}
            if a:
                self.add_aereoporto(a)

        def add_aereoporto(self, a: Aereoporto) -> None:
            self._aereoporto.add(a)

        def remove_aereporto(self, a: Aereoporto) -> None:
            self._aereoporto.remove(a)

        def __hash__(self) -> int:
            return hash((self.città(), self.aereoporto()))
        
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.città(), self.aereoporto()) == (other.città(), other.aereoporto())