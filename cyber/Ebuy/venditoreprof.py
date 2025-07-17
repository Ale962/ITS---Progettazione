from utente import *

class VenditoreProf(Utente):
    _vetrina: URL

    def __init__(self, username, registrazione, vetrina: URL):
        super().__init__(username, registrazione)
        self.set_vetrina(vetrina)

    def set_vetrina(self, vetrina) -> None:
        self._vetrina = vetrina
    
    def get_vetrina(self) -> URL:
        return self._vetrina
    
    def __repr__(self):
        return super().__repr__() + f'link vetrina: {self.get_vetrina()}'