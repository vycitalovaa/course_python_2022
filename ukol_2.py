sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte kód součástky:")
if kod_soucastky in sklad:
    mnozstvi_soucastek = int(input("Zadejte množství součástek: "))
    
else:
    print("Součástka není skladem!")
if mnozstvi_soucastek > sklad[kod_soucastky]:
    print("Součástky jsou dostupné pouze v omezeném množství kusů.")
    sklad.pop(kod_soucastky)
else:   
    print("Součástky máme!")
    sklad

