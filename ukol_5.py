teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerna_teplota = [(sum(den) / len(den)) for den in teploty]
print(prumerna_teplota)

ranni_teploty = [t[0] for t in teploty]
print(ranni_teploty)

nocni_teploty = [t[3] for t in teploty]
print(nocni_teploty)   

dvojice = [[t[1], t[3]] for t in teploty]
print(dvojice)

  




    







