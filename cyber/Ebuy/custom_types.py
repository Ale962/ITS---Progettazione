from typing import Self, Type
from typing import Any
import re
from enum import *

class RealGEZ(float):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    
class IntGEZ(int):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: int = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    
class RealGZ(float):
    # Tipo di dato Reale >= 0

    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super().__new__(cls, v)

        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo o uguale a 0!")
    

class URL(str):

    def __new__(cls, url: str) -> Self:
        pattern = r"https?://[^\s/$.?#].[^\s]*"

        if re.fullmatch(pattern, url):
            return url
        
        else:
            raise ValueError('La stringa inserita non è un url')
        

class Condizione(StrEnum):
    Usato_buone_condizioni = auto()
    Usato_ottime_condizioni = auto()
    Usato_accettabili_condizioni = auto()
    Usato_pessime_condizioni = auto()