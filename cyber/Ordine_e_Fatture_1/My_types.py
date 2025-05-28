from enum import *
from typing import Self
import re

# Creazione di una classe enumerativa, che si autodefinisce da sola con i suoi attributi di classe
class StatoOrdine(StrEnum):

    in_preparazione = auto()
    da_saldare = auto()
    saldato = auto()
    inviato = auto()


# Definizione della classe PositiveInt, solo interi positivi
class PositiveInt(int):

    # Creo un nuovo oggetto della classe usando __new__ invece di __init__, in questo caso perchè devo verificare che abbia delle determinate specifiche prima di creare l'oggetto, non uso init perchè non devo assegnare dei nuovi attributi in qianto essendo sotto classe di int li eredità da lì
    def __new__(cls, value: int|float|str|bool|Self) -> Self:


        # Specifico che qualsiasi cosa sia inserita come value venga trasoformato in un oggetto della classe int con tutte le sue proprietà
        n: int = super().__new__(cls, value)
        
        if n > 0:
            return n
        
        # Specifico solo il ValueError perchè il type e gli altri errori sono direttamente ereditati dalla super classe in
        raise ValueError(f"Number inserted {value} is negative")
    
# Creazione della classe codice Fiscale con uso di reggex
class CodiceFiscale(str):

    # definizione e crezione di un nuovo oggetto della classe CodiceFiscale, (di nuovo __new__ e non __init__ perchè devo creare l'oggetto più che definirne gli attributi, in quanto li eridità da str già tutti)
    def __new__(cls, cf: str) -> Self:

        # mi assicuri
        cff: str = cf.upper().strip()
        if re.fullmatch(r"^[A-Z]{6}[0-9]{2}[A-L]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$", cff):
            return super().__new__(cls, cff)
        

class Valuta(str):

    def __new__(cls, v: str|Self) -> Self:
        if re.fullmatch(r"^[A-Z]{3}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"Valuta non riconosciuta")
    
class Denaro:

    _importo: float
    valuta : Valuta

    def __init__(self, importo: float, valuta: Valuta):
        self._importo = importo
        self._valuta = valuta

    def importo(self) -> float:
        return self._importo
    
    def valute(self) -> Valuta:
        return self._valuta
    
    def __hash__(self) -> int:
        return hash((self.importo(), self.valute()))
    
    def __eq__(self, other: Self) -> bool:
        if hash(self) != hash(other):
            return False
        return self () == other.valute() and self.importo() == other.importo()
    
    def __add__(self, other: Self) -> Self:
        if self.valute() != other.valute():
            raise ValueError (f"The vlutes {self.valute()} and {other.valute()} are not the same")
        return self.importo() + other.importo()