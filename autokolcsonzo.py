from auto import Szemelyauto, Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    def berles_hozzaadasa(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam and all(b.auto.rendszam != rendszam or b.datum != datum for b in self.berlesek):
                berles = Berles(auto, datum)
                self.berlesek.append(berles)
                return berles.auto.berleti_dij
        return None

    def berles_lemondasa(self, rendszam, datum):
        for b in self.berlesek:
            if b.auto.rendszam == rendszam and b.datum == datum:
                self.berlesek.remove(b)
                return True
        return False

    def listaz_berlesek(self):
        return self.berlesek
