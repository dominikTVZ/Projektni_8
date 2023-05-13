from .korisnik import Korisnik
class PrivatniKorisnik(Korisnik):
    def __init__(self, email, telefon, ime, prezime):
        super().__init__(email, telefon)
        self.__ime = ime
        self.__prezime = prezime


    @property
    def ime(self):
        return self.__ime
    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    def ispis(self):
        print(f"Email: {self.email}")
        print(f"Telefon: {self.telefon}")
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
