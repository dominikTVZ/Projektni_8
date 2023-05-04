from artikl import get_artikl
from korisnik import get_korisnik
from kategorija import get_kategorija
from utilities import unos_datuma, unos_intervala
from .prodaja import Prodaja
def unos_prodaje(korisnici, kategorije, redni_broj):

    datum = unos_datuma("Unesite dan isteka prodaje: ")

    #ODABIR KORISNIKA
    print(f"Odaberite korisnika {redni_broj}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start = 1):
        print(get_korisnik(j, korisnik))

    odabrani_korisnik = unos_intervala(1, len(korisnici))-1
    korisnik = korisnici[odabrani_korisnik]

    #ODABIR KATEGORIJE
    print(f"Odaberite kategoriju {redni_broj}. prodaje: ")
    for i, kategorija in enumerate(kategorije, start = 1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = unos_intervala(1, len(kategorije))-1

    #ODABIR ARTIKLA
    print(f"Odaberite artikl {redni_broj}. prodaje: ")
    for k, artikl in enumerate(kategorije[odabrana_kategorija].artikli, start = 1):
        print(get_artikl(k, artikl))

    odabrani_artikl = unos_intervala(1, len(kategorije[odabrana_kategorija].artikli))-1
    artikl = kategorije[odabrana_kategorija].artikli[odabrani_artikl]

    return Prodaja(datum, korisnik, artikl)
