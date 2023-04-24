from math import ceil
cislo = input("Zadej svoje telefonní číslo:")
def user_number(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and "+420" == cislo[0:4]:
        return True
    else: 
        return False
        
def message(text_zpravy):
    pocet_znaku = len(text_zpravy)
    cena_za_sms = 3
    celkem = (ceil(pocet_znaku / 180)) * cena_za_sms
    return celkem       
    
if user_number(cislo):
    True
    text_zpravy = input("Zadej text zpravy:")
    celkem = message(text_zpravy)
    print(f"Zpráva bude stát {celkem} Kč.")
else: 
    False
    print(f"Telefonní číslo je ve špatném formátu.")

