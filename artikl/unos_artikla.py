from utilities import unos_pozitivnog_realnog_broja, unos_intervala
from .automobil import Automobil
from .stan import Stan

def unos_artikla(redni_broj):


    naslov = input(f"Unesite naslov {redni_broj}. artikla: ")
    opis = input(f"Unesite opis {redni_broj}. artikla: ")
    cijena = unos_pozitivnog_realnog_broja(f"Unesite cijenu {redni_broj}. artikla: ")

    print("Odaberite tip artikla: ")
    print("\t1. Stan")
    print("\t2. Automobil")

    tip_artikla = unos_intervala(1, 2)

    if tip_artikla == 1:
        kvadratura = unos_pozitivnog_realnog_broja(f"Unesite kvadraturu stana: ")
        return Stan(naslov, opis, cijena, kvadratura)

    if tip_artikla == 2:
        snaga = unos_pozitivnog_realnog_broja(f"Unesite snagu automobila: ")

        return Automobil(naslov, opis, cijena, snaga)
