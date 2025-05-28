from enum import *
import re

class Email:
    domini: list = [".it", ".com"] # aggiungere eventuali domini email
    VALID_EMAIL = re.compile(r"[A-Za-z0-9_-/\*#]+[@][A-Za-z0-9_-/\*#]+$") 
    def __init__(self, email, dominio, domini):
        if not Email.VALID_EMAIL.match(email) or dominio not in domini: # Email.VALID_EMAIL.match(email) esegue un match con la stringa data come valore email in modo che sia compatibile con la reggex di VALID_EMAIL dato come costante
            raise TypeError ("Types inserted not accepted")
        
        self.email = email
        self.dominio = dominio

    def get_email(self):
        return self.email + self.dominio
    
    def __hash__(self):
        return hash(self.get_email())

class CF:
    def __init__(self):
        pass

class Matricola:
    VALID_MATRICOLA = re.compile(r"[0-9]+")
    def __init__(self, matricola):
        pass

class Anno:
    def __init__(self):
        pass

class Gender(StrEnum):
    uomo = auto()
    donna = auto()


if __name__ == "__main__":

    print(Gender.uomo)
    print(type(Gender.uomo))
    print(Gender.donna.upper())
    print(Gender.donna.lower())

    print(Email("alessiocaico22@gmail", ".com"))