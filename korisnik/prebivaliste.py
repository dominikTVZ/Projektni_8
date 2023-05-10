class Prebivaliste:
    def __init__(self, mjesto):
        self.mjesto = mjesto


    @property
    def mjesto(self):
        return self.mjesto

    @mjesto.setter
    def mjesto(self, mjesto):
        self.mjesto = mjesto


