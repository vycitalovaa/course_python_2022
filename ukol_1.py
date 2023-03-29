moje_jmeno = "Anna.Vycitalova"
email = moje_jmeno + "@czechitas.cz"
print(email)

jmeno = input("Zadej jméno:")
prijmeni = input("Zadej příjmení:")
jmeno_a_prijmeni = jmeno + " " + pPrijmeni

print(jmeno_a_prijmeni)
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
print(jmeno[0] + ". " + prijmeni[0] + ".")

if len(jmeno) > 5:
    print(jmeno[0]+ ". " + prijmeni)
else: 
    print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
