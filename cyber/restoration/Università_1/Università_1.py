from __future__ import annotations
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
            if self in regione.citta():
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
    
    def regione(self)->Regione:
        return self._regione
    

class Regione:
    _nome: str # noto alla nascita
    _citta: list[Citta] # possibilmente non noto alla nascita
    _nazione: Nazione # noto alla nascita

    def __init__(self, nome: str, nazione: Nazione, citta: list[Citta] | None = None):
        self.set_nome(nome)
        self._citta = []
        if citta:
            for c in citta:
                self.add_citta(c)
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
            if self in nazione._regioni:
                nazione.remove_regione(self)
            else:
                pass
        except IndexError:
            pass
        if self._nome in nazione.regioni():
            raise ValueError('Non possono esistere due regione con lo stesso nome nella stessa nazione')
        self._nazione = nazione
        nazione.add_regione(self)

    def citta(self) -> frozenset[Citta]:
        return frozenset(self._citta)

    def nazione(self) -> Nazione:
        return self._nazione


class Nazione:
    _nome: str # noto alla nascita
    _regioni: list[Regione] # possibilmente non noto alla nascita

    def __init__(self, nome: str, regioni: list[Regione] | None = None):
        self.set_nome(nome)
        self._regioni = []
        if regioni:
            for r in regioni:
                self._regioni.append(r)
        
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def add_regione(self, regione: Regione) -> None:
        self._regioni.append(regione)

    def remove_regione(self, regione: Regione) -> None:
        self._regioni.remove(regione)

    def regioni(self) -> frozenset[Regione]:
        return frozenset(self._regioni)

class Facolta:
    _nome: str # noto alla nascita
    _corsi: list[Corso] # possibilmente non noto alla nascita

    def __init__(self, nome: str, corsi: list[Corso] | None = None):
        self.set_nome(nome)
        self._corsi = []
        if corsi:
            for c in corsi:
                self.add_corso(c)

    def name(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def corsi(self) -> frozenset[Corso]:
        return frozenset(self._corsi)
    
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
        self.set_facolta(facolta)
        self._insegnamenti = []
        if insegnamenti:
            for i in insegnamenti:
                self.add_insegnamento(i)
        
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

    def insegnamenti(self) -> frozenset[Insegnamento]:
        return frozenset(self._insegnamenti)

class Insegnamento:
    _nome: str # noto alla nascita
    _codice: str # immutabile e noto alla nascita
    _durata: time # noto alla nascita
    _corsi: list[Corso] # noto alla nascita

    def __init__(self, nome: str, codice: str, durata: time, corsi: list[Corso]):
        self.set_nome(nome)
        self._codice = codice
        self.set_durata(durata)
        self._corsi = []
        if corsi:
            for c in corsi:
                self.add_corso(c)

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

    def corsi(self) -> frozenset[Corso]:
        return frozenset(self._corsi)
    
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
    _citta: Citta
    

    def __init__(self, nome: str, cognome: str, codice_fiscale: str, is_studente: bool, is_professore: bool, citta: Citta, matricola: str | None = None, data_iscrizione: datetime | None = None, corso_superato: dict[Corso, Voto] | None = None, facolta: Facolta | None = None, insegnamenti: list[Insegnamento] | None = None):
        self.set_nome(nome)
        self.set_cognome(cognome)
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
                    self.add_corso_superato(c, v)
            if facolta:
                self.set_facolta(facolta)
            else:
                raise RuntimeError('Lo studente deve avere per forza una facolta una volta che si iscrive')
            if not (matricola or data_iscrizione):
                raise ValueError('Lo studente deve avere per forza una matricola e una data di iscrizione alla facoltà')
        if self._is_professore:
            if insegnamenti:
                for i in insegnamenti:
                    self.add_corso_insegnato(i)
        self._citta = citta
        regione: Regione = citta.regione()
        nazione: Nazione = regione.nazione()
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
    
    def luogo_di_nascita(self) -> frozenset[tuple]:
        return frozenset(self._luogo_di_nascita.items())
            
    
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
        list_corsi_superati = []
        if self._is_studente:
            for c,v in self._corsi_superati.items():
                corso: tuple = (c, v)
                list_corsi_superati.append(corso)
            return frozenset(list_corsi_superati)
        else:
            print(f'La persona {self._nome} {self._cognome} non è uno studente, impossibile accedere ai corsi superati')

    def insegnamenti(self) -> frozenset[Insegnamento]:
        if self._is_professore:
            return frozenset(self._insegnamenti)
        else:
            print(f'La persona {self._nome} {self._cognome} non è un insegnante, impossibile accedere ai corsi insegnati')

    def facolta(self) -> Facolta:
        if self._is_studente:
            return self._facolta
        
    def set_facolta(self, facolta: Facolta) -> None:
        self._facolta = facolta


if __name__ == '__main__':
    italia = Nazione("Italia")
    lombardia = Regione("Lombardia", italia)
    milano = Citta("Milano", lombardia)

    ingegneria = Facolta("Ingegneria")
    corso_a = Corso("Programmazione", ingegneria)
    ingegneria.add_corso(corso_a)

    insegnamento_prog = Insegnamento("Python", "INF101", time(2, 0), [corso_a])
    corso_a.add_insegnamento(insegnamento_prog)

    studente = Persona(
        nome="Mario",
        cognome="Rossi",
        codice_fiscale="RSSMRA80A01H501U",
        is_studente=True,
        is_professore=False,
        citta=milano,
        matricola="123456",
        data_iscrizione=datetime(2022, 9, 1),
        corso_superato={corso_a: Voto(28)},
        facolta=ingegneria
    )

    professore = Persona(
        nome="Luca",
        cognome="Verdi",
        codice_fiscale="VRDLUC70A01H501U",
        is_studente=False,
        is_professore=True,
        citta=milano,
        insegnamenti=[insegnamento_prog]
    )

    print(studente.nome(), studente.cognome(), studente.matricola())
    print([c.nome() for c, v in studente.corsi_superati()])
    print(professore.nome(), professore.cognome(), [i.nome() for i in professore.insegnamenti()])
    print(milano.nome(), milano.regione().nome(), milano.regione().nazione().nome())