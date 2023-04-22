from math import ceil
cislo = input("Zadej svoje telefonní číslo:")
def user_number(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and "+420" == cislo[0:4]:
        return True
    else: 
        return False
        exit()  

print(user_number(cislo))
text_zpravy = input("Zadej text zprávy:")
def message(text_zpravy):
    pocet_znaku = len(text_zpravy)
    cena_za_sms = 3
    celkem = ceil(pocet_znaku / 180) * cena_za_sms
    return celkem        
    print(f"{message}")

