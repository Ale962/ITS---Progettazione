from datetime import date
from custom_types import *
from impiegato import Impiegato
from persona import Persona
from posizione_militare import PosizioneMilitare
from progetto import Progetto
from res_prog import res_prog
from studente import Studente

if __name__ == '__main__':

    # Crea un codice fiscale valido
    cf = CodiceFiscale("RSSMRA85T10A562S") 

    # Crea un indirizzo valido
    indirizzo = Indirizzo("Via Roma", "12A", CAP("00100"))

    # Crea un impiegato uomo
    imp = Impiegato(
        stipendio=RealGEZ(2500.50),
        ruolo=Ruolo.direttore,
        is_responsabile=True,
        nome="Mario",
        cognome="Rossi",
        cf=cf,
        nascita=date(1985, 10, 10),
        genere=Genere.uomo,
        posizione_militare=PosizioneMilitare.Capitano
    )

    # Crea un progetto
    proj = Progetto("AI Transformation")

    # Collega impiegato e progetto tramite res_prog
    res_prog.add_link(imp, proj)

    # Mostra i link creati
    print("Collegamenti attuali:")
    for k, v in res_prog.res_prog_link.items():
        print(k, "->", v)

    # Crea un nuovo link identico per rimozione
    link_to_remove = res_prog._link(imp, proj)

    # Rimuovi il link
    res_prog.remove_link(link_to_remove)

    # Mostra i link rimasti
    print("\nDopo rimozione:")
    for k, v in res_prog.res_prog_link.items():
        print(k, "->", v)
