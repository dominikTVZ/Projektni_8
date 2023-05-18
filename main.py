from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from datetime import date
from korisnik import unos_korisnika, ispis_svih_korisnika
from kategorija import unos_kategorije, ispis_svih_kategorija
from prodaja import unos_prodaje, ispis_svih_prodaja
from utilities import unos_intervala

korisnici = []
kategorije = []
prodaje = []

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Objeknto')
        self.setWindowIcon(QtGui.QIcon('images/python.png'))


    def initUI(self):
        offset = 30
        self.font = QtGui.QFont('Helvatica', 10)

    # Input tip korisnika
        self.tip_korisnika = QtWidgets.QComboBox(self)

        for korisnik in TipKorisnika:
            self.tip_korisnika.addItem(str(korisnik.value))

        self.tip_korisnika.setGeometry(QtCore.QRect(150, offset, 150, 25))
        self.tip_studenta.currentTextChanged.connect(self.on_combobox_changed)
        