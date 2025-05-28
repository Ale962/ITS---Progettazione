
class Nazione:
    _name: str # noto alla nascità

    def name(self) -> str:
        return self._name
    
    def set_name(self, n: str) -> None:
        self._name = n

    def __init__(self, name: str):
        
        self.set_name(name)