from .artikl import Artikl
class Stan(Artikl):
    def __init__(self, naslov, opis, cijena, kvadratura):
        super().__init__(naslov, opis, cijena)
        self.__kvadratura = kvadratura

    def ispis(self):
        return f'{self.naslov}, {self.opis}, {self.cijena}, {self.kvadratura}'
        """
        print(f"\tInformacije o stanu: ")
        print(f"\tNaslov: {self.naslov}")
        print(f"\tOpis: {self.opis}")
        print(f"\tCijena: {self.cijena}")
        print(f"\tKvadratura: {self.__kvadratura}")
        """