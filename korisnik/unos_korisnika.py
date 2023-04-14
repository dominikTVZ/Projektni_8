
def unos_korisnika(redni_broj):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {redni_broj}. korisnika: ").title()
    korisnik['prezime'] = input(f"Unesite prezime {redni_broj}. korisnika: ").title()
    korisnik['telefon'] = int(input(f"Unesite telefon {redni_broj}. korisnika: "))
    korisnik['email'] = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    return korisnik
