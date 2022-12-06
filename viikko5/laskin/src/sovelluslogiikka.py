class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        
class BinaariOperaatio:
    def __init__(self, io):
        self.io = io
        self.luku1 = 0
        self.luku2 = 0

    def suorita(self):
        self.luku1 = int(self.io.lue("Luku 1:"))
        self.luku2 = int(self.io.lue("Luku 2:"))

        self.io.kirjoita(f"Vastaus: {self.laske()}")

    def laske(self):
        return 0

        
class Erotus:
    def __init__(self, io):
        self.io = io
        
    def suorita(self):
        luku = int(self.io.lue_syote)
