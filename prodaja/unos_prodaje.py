from artikl import get_artikl
from korisnik import get_korisnik
from kategorija import get_kategorija
from datetime import date

def unos_prodaje(korisnici, kategorije, redni_broj):
    prodaja = {}
    dan = int(input(f"Unesite dan isteka {redni_broj}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {redni_broj}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {redni_broj}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

    #ODABIR KORISNIKA
    print(f"Odaberite korisnika {redni_broj}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start = 1):
        print(get_korisnik(j, korisnik))

    odabrani_korisnik = int(input("Odabrani korisnik: "))-1

    #ODABIR KATEGORIJE
    print(f"Odaberite kategoriju {redni_broj}. prodaje: ")
    for i, kategorija in enumerate(kategorije, start = 1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = int(input("Odabrana kategorija: "))-1

    #ODABIR ARTIKLA
    print(f"Odaberite artikl {redni_broj}. prodaje: ")
    for k, artikl in enumerate(kategorije[odabrana_kategorija]['artikli'], start = 1):
        print(get_artikl(k, artikl))

    odabrani_artikl = int(input("Odabrani artikl: "))-1

    prodaja['artikl'] = kategorije[odabrana_kategorija]['artikli'][odabrani_artikl]
    prodaja['korisnik'] = korisnici[odabrani_korisnik]
    return prodaja
