from Città import Città
from Nazione import Nazione
from typing import Any

class cit_naz:
    class _link:
        _città: Città # noto alla nascità
        _nazione: Nazione # noto alla nascità

        def città(self) -> frozenset[Città]:
            return self._città
        
        def nazione(self) -> frozenset[Nazione]:
            return self._nazione
        
        def __init__(self, c: set[Città], n: set[Nazione]):
            if not c:
                raise RuntimeError("Must contain at last one city")
            self._città: set[Città] = c
            if not n:
                raise RuntimeError("Must contain at last one nation")
            self._nazione: set[Nazione] = n

        def add_city(self, c: Città) -> None:
            self._città.add(c)

        def remove_city(self, c: Città) -> None:
            if len(self._città) > 1:
                self._città.remove(c)
            else:
                raise RuntimeError("Must have at last one city")

        def add_nation(self, n: Nazione) -> None:
            self._nazione.add(n)

        def remove_nation(self, n: Nazione) -> None:
            if len(self._nazione) > 1:
                self._nazione.remove(n)
            else:
                raise RuntimeError("Must have at last one nation")

        def __hash__(self) -> int:
            return hash((self.città(), self.nazione()))
        
        def __eq__(self, other:Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return (self.città(), self.nazione()) == (other.città(), other.nazione())