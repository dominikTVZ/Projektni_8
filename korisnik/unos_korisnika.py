from utilities import unos_pozitivnog_cijelog_broja
from .korisnik import Korisnik
def unos_korisnika(redni_broj):

    ime = input(f"Unesite ime {redni_broj}. korisnika: ").title()
    prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").title()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika")
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()

    return Korisnik(ime, prezime, email, telefon)

