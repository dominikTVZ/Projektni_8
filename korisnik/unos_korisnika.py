from utilities import unos_pozitivnog_cijelog_broja
from .korisnik import Korisnik
from .adresa import Adresa

def unos_korisnika(redni_broj):

    ime = input(f"Unesite ime {redni_broj}. korisnika: ").title()
    prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").title()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    ulica = input(f"Unesite ulicu {redni_broj}. korisnika: ")
    kucni_broj = int(input(f"Unesite kucni broj {redni_broj}. korisnika: "))
    grad = input(f"Unesite grad {redni_broj}. korisnika: ")




    adresa = Adresa(ulica, kucni_broj, grad)

    return Korisnik(ime, prezime, email, telefon, adresa)

