from .artikl import Artikl
from .vozilo import Vozilo
class Automobil(Artikl, Vozilo):
    def __init__(self, naslov, opis, cijena, snaga):
        super().__init__(naslov, opis, cijena)
        self.snaga = snaga



    def ispis(self):
        print(f"\tInformacije o automobilu: ")
        print(f"\tNaslov: {self.naslov}")
        print(f"\tOpis: {self.opis}")
        print(f"\tCijena: {self.cijena}")
        print(f"\tCijena osiguranja automobila: {self.cijena_osiguranja(self.snaga)}")
