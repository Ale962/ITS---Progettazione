from custom_types import *
from datetime import datetime

class Utente:
    _username: str # immutabile
    _registrazione: datetime # immutabile

    def __init__(self,username: str, registrazione: datetime):
        self._username = username
        self._registrazione = registrazione
    
    def get_username(self) -> str:
        return self._username
    
    def get_registrazione(self) -> datetime:
        return self._registrazione

    def __repr__(self):
        return f'Username: {self.get_username()}, iscritto: {self.get_registrazione()}'
    