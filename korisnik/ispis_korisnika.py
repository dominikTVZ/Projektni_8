



def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik.ime} {korisnik.prezime}"

def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()