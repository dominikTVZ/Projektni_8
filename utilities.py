from datetime import date
from iznimke import IznimkaPrazanTekst, IznimkaTelefon
def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception(f"Unesite cijeli pozitivan broj.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception(f"Unesite pozitivan realni broj.")

        except ValueError:
            print('Unesli ste znak a ne realni broj.')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):
    while True:
        try:
            dan = int(input(poruka))
            mjesec = int(input(f'Unesite mjesec isteka prodaje: '))
            godina = int(input(f'Unesite godinu isteka prodaje: '))
            datum = date(godina, mjesec, dan)


        except Exception as e:
            print(e)

        else:
            return datum
def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def provjera_korisnickog_unosa(telefon, email, ime, prezime):
    try:
        if len(email) == 0 or len(ime) == 0 or len(prezime) == 0:
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)

    try:
        if len(telefon) != 8:
            raise IznimkaTelefon()
    except IznimkaTelefon as e:
        return str(e)

    try:
        broj = int(telefon)
    except ValueError:
        return str('Telefon mora biti broj')

    else:
        return None







