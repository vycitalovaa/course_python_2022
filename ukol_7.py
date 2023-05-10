class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = int(najete_km)
        self.dostupne = True

    def puj_auto(self):
        self.dostupne = False
    
    def __str__(self):
        if self.dostupne:
            pujceno_zprava = "Vozidlo není k dispozici"
        else:
            pujceno_zprava = "Potvrzuji zapůjčení vozidla"

    def info(self):
        return f"Máme vozidlo {self.typ_vozidla} s registrační značkou {self.registracni_znacka}."
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
print(auto2.info())
auta = [auto1, auto2]

pujcovane_vozidlo = input("Zadej značku vozidla, které si chceš půjčit:")
if pujcovane_vozidlo == "Peugeot":
    def info(self):
        return f"Máme vozidlo {self.auto1}. {self.pujceno_zprava}"
elif pujcovane_vozidlo == "Škoda":
    def info(self):
        return f"Máme vozidlo {self.auto2}. {self.pujceno_zprava}"
else:
    def info(self):
        return f"Vozidlo nemáme. {self.pujceno_zprava}"