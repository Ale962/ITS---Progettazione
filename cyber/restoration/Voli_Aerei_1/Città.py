from My_Types import IntGZ

class Città:
    _name: str # noto alla nascità
    _abitanti: IntGZ # noto alla nascità

    def name(self) -> str:
        return self._name
    
    def abitanti(self) ->IntGZ:
        return self._abitanti
    
    def set_name(self, n: str) -> None:
        self._name = n

    def set_abitanti(self, a: IntGZ) -> None:
        self._abitanti = a

    def __init__(self, name: str, abitanti: IntGZ):
        
        self.set_name(name)
        self.set_abitanti(abitanti)