class Adresa:
    def __init__(self, ulica, kucni_broj, grad):
        self.__ulica = ulica
        self.__kucni_broj = kucni_broj
        self.__grad = grad



    @property
    def ulica(self):
        return self.__ulica

    @ulica.setter
    def ulica(self, ulica):
        self.__ulica = ulica

    @property
    def kucni_broj(self):
        return self.__kucni_broj

    @kucni_broj.setter
    def ulica(self, kucni_broj):
        self.__kucni_broj = kucni_broj

    @property
    def grad(self):
        return self.__grad

    @grad.setter
    def grad(self, grad):
        self.__grad= grad

    def ispis(self):
        print("Informacije o adresi: ")
        print(f"Ulica: {self.__ulica}")
        print(f"Kucni broj : {self.__kucni_broj}")
        print(f"Grad: {self.__grad}")
