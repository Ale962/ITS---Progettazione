from custom_types import *
from datetime import date, datetime
from impiegato import Impiegato
from progetto import Progetto
from dipartimento import Dipartimento
from coinvolto import coinvolto
from afferenza import afferenza
from direzione import direzione

if __name__ == '__main__':
    tel3: Telefono = Telefono("3334445566")
    tel4: Telefono = Telefono("3337778899")
    ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "205b",
                            CAP("00144"))

    alice: Impiegato = Impiegato("Alice", "Alessi",
                                date(year=1990, month=12, day=31),
                                RealGEZ(18000))
    print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

    bob: Impiegato = Impiegato("Bob", "Burnham",
                                date(year=1997, month=10, day=11),
                                RealGEZ(19000))
    print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")


    dip3: Dipartimento = Dipartimento("Vendite", tel3, ind)

    print(f"Ho creato il dipartimento {dip3}")


    dip4: Dipartimento = Dipartimento("Acquisti", tel4, None)
    print(f"Ho creato il dipartimento {dip4}")

    t: frozenset[Telefono] = dip3.telefoni()

    print("dip1.telefoni() = " + str(dip3.telefoni()))

    dip3.add_telefono(Telefono("3481265413"))

    print("dip1.telefoni() = " + str(dip3.telefoni()))



    pegaso: Progetto = Progetto(nome="Pegaso", budget=45_000)


    # --- Create base objects ---
    tel = Telefono("3331234567")
    cap = CAP("20100")
    indirizzo = Indirizzo("Via Roma", "10", cap)
    imp1 = Impiegato("Luca", "Rossi", date(1990, 5, 17), RealGEZ(3000))
    imp2 = Impiegato("Anna", "Bianchi", date(1985, 3, 12), RealGEZ(3200))
    proj1 = Progetto("AI Platform", RealGEZ(100000))
    proj2 = Progetto("Web Redesign", RealGEZ(20000))
    dip1 = Dipartimento("Informatica", tel, indirizzo)
    dip2 = Dipartimento("Design", Telefono("3339876543"), None)

    print("Creati impiegati, progetti e dipartimenti.")

    # --- Test direzione ---
    direzione.add_link(dip1, imp1)
    direzione.add_link(dip2, imp1)
    print("Impiegato imp1 assegnato come direttore a dip1 e dip2.")

    try:
        direzione.add_link(dip1, imp2)
    except ValueError as e:
        print("Corretto errore: tentativo di riassegnare un dipartimento già diretto:", e)

    for x in direzione.direnzione_link:
        print("Direzione:", x)

    # Rimuovi uno dei due dipartimenti da imp1
    for l in list(direzione.direnzione_link[0]["Link"]):
        if l.dipartimento() == dip1:
            direzione.remove_link(l)
    print("Rimossa direzione imp1 da dip1.")

    for x in direzione.direnzione_link:
        print("Direzione dopo rimozione:", x)

    # --- Test coinvolto ---
    coinvolto.add_link(imp1, proj1)
    coinvolto.add_link(imp2, proj2)
    print("Collegati impiegati a progetti.")

    print("Link coinvolti:", coinvolto.coinvolto_link)

    # Rimozione
    link_to_remove = list(coinvolto.coinvolto_link.keys())[0]
    coinvolto.remove_link(link=link_to_remove)
    print("Rimosso un link da coinvolto.")

    print("Link coinvolti dopo rimozione:", coinvolto.coinvolto_link)

    # --- Test afferenza ---
    afferenza.add_link(dip1, imp1, datetime(2023, 6, 1))
    afferenza.add_link(dip1, imp2, datetime(2024, 1, 10))
    print("Aggiunti impiegati al dipartimento con afferenza.")

    for a in afferenza.afferenza_link:
        print("Afferenza:", a)

    # Rimozione afferenza imp1
    link_to_remove = None
    for l in afferenza.afferenza_link[0]["Link"]:
        if l.impiegato() == imp1:
            link_to_remove = l
    if link_to_remove:
        afferenza.remove_link(link_to_remove)
        print("Rimossa afferenza imp1 da dip1.")

    for a in afferenza.afferenza_link:
        print("Afferenza dopo rimozione:", a)
