class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = int(najete_km)
        self.dostupne = True

    def pujc_auto(self):        
        if self.dostupne:
            self.dostupne = False 
            print("Vozidlo je k zapůjčení")            
        else: 
            print("Vozidlo není dostupné")
       


    def getInfo(self):
        return f"Máme vozidlo {self.typ_vozidla} s registrační značkou {self.registracni_znacka}."

auto_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto_2 = Auto("1P3 4747", "Škoda Octavia", 41253)


pujcovane_vozidlo = input("Zadej značku vozidla, které si chceš půjčit:")
if pujcovane_vozidlo == "Peugeot":
    print(auto_1.pujc_auto())
    print(auto_1.getInfo())
    
elif pujcovane_vozidlo == "Škoda":
    print(auto_2.pujc_auto())
    print(auto_2.getInfo())
else:
    print(f"Půjčované vozidlo není k dipozici")
pujcovane_vozidlo = input("Zadej značku vozidla, které si chceš půjčit:")
if pujcovane_vozidlo == "Peugeot":
    print(auto_1.pujc_auto())
    print(auto_1.getInfo())
    
elif pujcovane_vozidlo == "Škoda":
    print(auto_2.pujc_auto())
    print(auto_2.getInfo())
else:
    print(f"Půjčované vozidlo není k dipozici")



