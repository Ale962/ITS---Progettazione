from My_types import *
from datetime import datetime, time

class Citta:
    _nome: str # noto alla nascita
    _regione: Regione # possibilemente non noto alla nascita

    def __init__(self, nome: str, regione: Regione):
        self.set_nome(nome)
        self.set_regione(regione)

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_regione(self, regione: Regione) -> None:
        try:
            if self._nome in regione._citta:
                self._regione.remove_citta(self)
            else:
                pass
        except IndexError:
            pass
        if self._nome in regione._citta:
            raise ValueError('Non possono esistere due città con lo stesso nome nella stessa regione')
        self._regione = regione
        regione.add_citta(self)

    def nome(self) -> str:
        return self._nome
    
    def regione(self)->str:
        return self._regione
    

class Regione:
    _nome: str # noto alla nascita
    _citta: list[Citta] # possibilmente non noto alla nascita
    _nazione: Nazione # noto alla nascita

    def __init__(self, nome: str, nazione: Nazione, citta: list[Citta] | None = None):
        self.set_nome(nome)
        self._citta = []
        if citta:
            self.add_citta(c for c in citta)
        self.set_nazione(nazione)

    def add_citta(self, citta: Citta) -> None:
        self._citta.append(citta)
    
    def remove_citta(self, citta: Citta) -> None:
        self._citta.remove(citta)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome) -> None:
        self._nome = nome

    def set_nazione(self, nazione: Nazione) -> None:
        try:
            if self._nome in nazione._regioni:
                nazione.remove_regione(self)
            else:
                pass
        except IndexError:
            pass
        if self._nome in nazione._regione:
            raise ValueError('Non possono esistere due regione con lo stesso nome nella stessa nazione')
        self._nazione = nazione
        nazione.add_regione(self)

    def citta(self) -> list[Citta]:
        return self._citta



class Nazione:
    _nome: str # noto alla nascita
    _regioni: list[Regione] # possibilmente non noto alla nascita

    def __init__(self, nome: str, regioni: list[Regione] | None = None):
        self.set_nome(nome)
        self._regioni = []
        if regioni:
            self._regioni.append(r for r in regioni)
        
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def add_regione(self, regione: Regione) -> None:
        self._regioni.append(regione)

    def remove_regione(self, regione: Regione) -> None:
        self._regioni.remove(regione)

class Facolta:
    _nome: str # noto alla nascita
    _corsi: list[Corso] # possibilmente non noto alla nascita

    def __init__(self, nome: str, corsi: Corso | None = None):
        self.set_nome(nome)
        self._corsi = []
        if corsi:
            self.add_corso(c for c in corsi)

    def name(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def corsi(self) -> list[Corso]:
        return self._corsi
    
    def add_corso(self, corso: Corso) -> None:
        self._corsi.append(corso)

    def remove_corso(self, corso: Corso) -> None:
        self._corsi.remove(corso)


class Corso:
    _nome: str # noto alla nascita
    _facolta: Facolta # noto alla nascita
    _insegnamenti: list[Insegnamento]|None # possibilmente non noto alla nascita

    def __init__(self, nome: str, facolta: Facolta, insegnamenti: list[Insegnamento]|None = None):
        self.set_nome(nome)
        self._set_facolta(facolta)
        self._insegnamenti = []
        if insegnamenti:
            self.add_insegnamento(i for i in insegnamenti)
        
    def nome(self)->str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def facolta(self) -> Facolta:
        return self._facolta
    
    def set_facolta(self, facolta: Facolta) -> None:
        self._facolta = facolta

    def add_insegnamento(self, insegnamento: Insegnamento) -> None:
        self._insegnamenti.append(insegnamento)

    def remove_insegnamento(self, insegnamento: Insegnamento) -> None:
        self._insegnamenti.remove(insegnamento)

    def insegnamenti(self) -> list[Insegnamento]:
        return self._insegnamenti

class Insegnamento:
    _nome: str # noto alla nascita
    _codice: str # immutabile e noto alla nascita
    _durata: time # noto alla nascita
    _corsi: list[Corso] # noto alla nascita

    def __init__(self, nome: str, codice: str, durata: time, corsi: list[Corso]):
        self.set_nome(nome)
        self._codice(codice)
        self.set_durata(durata)
        self._corsi = []
        if corsi:
            self.add_corso(c for c in corsi)

    def nome(self)->str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def durata(self)->time:
        return self._durata
    
    def set_durata(self, durata: time) -> None:
        self._durata = durata

    def add_corso(self, corso: Corso) -> None:
        self._corsi.append(corso)

    def remove_corso(self, corso: Corso) -> None:
        self._corsi.remove(corso)

    def corsi(self) -> list[Corso]:
        return self._corsi
    
    def codice(self) -> str:
        return self._codice
    
class Persona:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _codice_fiscale: str # immutabile, noto alla nascita
    _is_studente: bool # noto alla nascita
    _is_professore: bool # noto alla nascita
    _matricola: str | None # immutabile possibilmente non noto alla nascita
    _data_iscrizione: str | None # immutabile possibilmente non noto alla nascita
    _corsi_superati: dict[Corso, Voto] | None # non noto alla nascita
    _facolta: Facolta | None # noto alla nascita
    _insegnamenti: list[Insegnamento] | None # non noto alla nascita
    _luogo_di_nascita: dict[str, Citta|Regione|Nazione] # immutabile, noto alla nascita
    

    def __init__(self, nome: str, cognome: str, codice_fiscale: str, is_studente: bool, is_professore: bool, citta: Citta, regione: Regione, nazione: Nazione, matricola: str | None = None, data_iscrizione: datetime | None = None, corso_superato: dict[Corso, Voto] | None = None, facolta: Facolta | None = None, insegnamenti: list[Insegnamento] | None = None):
        self.set_nome(nome)
        self.set_cognome(nome)
        self.set_codice_fiscale(codice_fiscale)
        self.set_is_studente(is_studente)
        self.set_is_professore(is_professore)
        self._corsi_superati = {}
        self._insegnamenti = []
        if self._is_studente:
            self._matricola = matricola
            self._data_iscrizione = data_iscrizione
            if corso_superato:
                for c, v in corso_superato.items():
                    self._add_corso_superato(c, v)
            if facolta:
                self.set_facolta(facolta)
            else:
                raise RuntimeError('Lo studente deve avere per forza una facolta una volta che si iscrive')
            if not (matricola or data_iscrizione):
                raise ValueError('Lo studente deve avere per forza una matricola e una data di iscrizione alla facoltà')
        if self._is_professore:
            if insegnamenti:
                self.add_corso_insegnato(c for c in insegnamenti)
        self._luogo_di_nascita = {'citta': citta, 'regione': regione, 'nazione': nazione}

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_codice_fiscale(self, codice_fiscale: str) -> None:
        self._codice_fiscale = codice_fiscale

    def set_is_studente(self, is_student: bool) -> None:
        self._is_studente = is_student
    
    def set_is_professore(self, is_professore: bool) -> None:
        self._is_professore = is_professore

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def codice_fiscale(self) -> str:
        return self._codice_fiscale
    
    def is_studente(self) -> bool:
        return self._is_studente
    
    def is_professore(self) -> bool:
        return self._is_professore
    
    def luogo_di_nascita(self) -> dict:
        return self._luogo_di_nascita
    
    def matricola(self) -> str:
        if self._is_studente:
            return self._matricola
        else:
            print(f'Persona {self._nome} {self._cognome} non identificata come studente, non è possibile accedere ad alcuna matricola')

    def data_iscrizione(self) -> str:
        if self._is_studente:
            return self._data_iscrizione
        else:
            print(f'Persona {self._nome} {self._cognome} non identificata come studente, non è possibile accedere ad alcuna data di iscrizione')
    
    def add_corso_superato(self, corso: Corso, voto: Voto) -> None:
        if corso in self._corsi_superati:
            raise ValueError(f'Il corso {corso} è già presente nella raccolta corsi superati, non è possibile superare due volte lo stesso corso')
        else:
            self._corsi_superati[corso] = voto

    def remove_corso_superato(self, corso: Corso, voto: Voto) -> None:
        if corso not in self._corsi_superati:
            raise RuntimeError(f'Il corso {corso} non è presente nella racccolta corsi superati')
        else:
            self._corsi_superati.pop(corso)
    
    def add_corso_insegnato(self, insegnamento: Insegnamento) -> None:
        self._insegnamenti.append(insegnamento)

    def remove_corso_insegnato(self, insegnamento: Insegnamento) -> None:
        self._insegnamenti.remove(insegnamento)

    def corsi_superati(self) -> dict[Corso, Voto]:

        if self._is_studente:
            return self._corsi_superati
        else:
            print(f'La persona {self._nome} {self._cognome} non è uno studente, impossibile accedere ai corsi superati')

    def insegnamenti(self) -> list[Insegnamento]:
        if self._is_professore:
            return self._insegnamenti
        else:
            print(f'La persona {self._nome} {self._cognome} non è un insegnante, impossibile accedere ai corsi insegnati')

    def facolta(self) -> Facolta:
        if self._is_studente:
            return self._facolta
        
    def set_facolta(self, facolta: Facolta) -> None:
        self._facolta = facolta