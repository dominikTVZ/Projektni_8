from utilities import unos_pozitivnog_cijelog_broja
from .korisnik import Korisnik
from .adresa import Adresa
from .prebivaliste import Prebivaliste
def unos_korisnika(redni_broj):

    ime = input(f"Unesite ime {redni_broj}. korisnika: ").title()
    prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").title()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    ulica = input(f"Unesite ulicu {redni_broj}. korisnika: ")
    kucni_broj = int(input(f"Unesite kucni broj {redni_broj}. korisnika: "))
    grad = input(f"Unesite grad {redni_broj}. korisnika: ")
    mjesto = input(f"Unesite mjesto prebivalista {redni_broj}. korisnika: ")

    prebivaliste = Prebivaliste(mjesto)

    adresa = Adresa(ulica, kucni_broj, grad, prebivaliste)

    return Korisnik(ime, prezime, email, telefon, adresa)

