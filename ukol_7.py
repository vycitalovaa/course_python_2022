class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = int(najete_km)
        self.dostupne = True

    def pujc_auto(self):
        self.dostupne = False        
        if self.dostupne:
            return f"Vozidlo není k dispozici"
        else:
            return f"Potvrzuji zapůjčení vozidla"

    def getInfo(self):
        return f"{self.typ_vozidla} s registrační značkou {self.registracni_znacka}"
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pujcovane_vozidlo = input("Zadej značku vozidla, které si chceš půjčit:")
if pujcovane_vozidlo == "Peugeot":
    print(f"Vozidlo {auto1.getInfo()}. {auto1.pujc_auto()}.")
elif pujcovane_vozidlo == "Škoda":
    print(f"Vozidlo {auto1.getInfo()}. {auto2.pujc_auto()}.")
else:
    print(f"Vozidlo nemáme.")

    
        
