from artikl import unos_artikla
from .kategorija import Kategorija

def unos_kategorije(redni_broj):

    naziv = input(f"Unesite naziv {redni_broj}. kategorije: ")
    artikli = []

    broj_artikala = int(input("Odaberite broj artikala: "))
    for j in range(1, broj_artikala+1):
        artikl = unos_artikla(j)
        artikli.append(artikl)
    return Kategorija(naziv, artikli)
