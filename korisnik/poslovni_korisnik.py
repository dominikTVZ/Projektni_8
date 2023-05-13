from .korisnik import Korisnik
class PoslovniKorisnik(Korisnik):
    def __init__(self, email ,telefon, naziv, web):
        super().__init__(email, telefon)
        self.naziv = naziv
        self.web = web

    @property
    def naziv(self):
        return self.naziv

    @naziv.setter
    def naziv(self, naziv):
        self.naziv = naziv

    @property
    def web(self):
        return self.web

    @web.setter
    def web(self, web):
        self.web = web

    def ispis(self):
        print('Informacije o poslovnom korisniku: ')
        print(f'\tNaziv: {self.naziv}')
        print(f'\tWeb: {self.web}')
        print(f'\tTelefon: {self.telefon}')
        print(f'\tEmail: {self.email}')