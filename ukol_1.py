moje_jmeno = "Anna.Vycitalova"
email = moje_jmeno + "@czechitas.cz"
print(email)


Jmeno = input("Zadej jméno:")
Prijmeni = input("Zadej příjmení:")
jmeno_a_prijmeni = Jmeno + " " + Prijmeni
print(jmeno_a_prijmeni)
print(jmeno_a_prijmeni .upper())
print(jmeno_a_prijmeni .lower())
print(Jmeno[0] .upper() + Jmeno[1:] .lower() + " " + Prijmeni[0] .upper() + Prijmeni[1:] .lower())
print(Jmeno[0] + ". " + Prijmeni[0] + ".")
if len(Jmeno) > 5:
    print(Jmeno[0]+ ". " + Prijmeni)
else: print(Jmeno[0] .upper() + Jmeno[1:] .lower() + " " + Prijmeni[0] .upper() + Prijmeni[1:] .lower())
