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
if mnozstvi_soucastek <= sklad[kod_soucastky]:
        print("Součástky máme!")