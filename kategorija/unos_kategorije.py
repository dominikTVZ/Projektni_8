from artikl import unos_artikla
def unos_kategorije(redni_broj):
    kategorija = {}
    artikli = []
    kategorija['naziv'] = input(f"Unesite naziv {redni_broj}. kategorije: ")

    broj_artikala = int(input("Odaberite broj artikala: "))
    for j in range(1, broj_artikala+1):
        artikl = unos_artikla(j)
        artikli.append(artikl)

    kategorija['artikli'] = artikli
    return kategorija
