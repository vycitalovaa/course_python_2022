class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = int(najete_km)
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne :
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozilda"
        else:
            return f"Vozidlo není dostupné"
        if pujcovane_vozidlo == "Peugeot":    
            return f"Máme vozidlo {self.auto1}. {self.dostupne}"
        elif pujcovane_vozidlo == "Škoda":        
            return f"Máme vozidlo {self.auto2}. {self.dostupne}"     
            

    def getInfo(self):
        return f"{self.typ_vozidla} s registrační značkou {self.registracni_znacka}"
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pujcovane_vozidlo = input("Zadej značku vozidla, které si chceš půjčit:")









        
