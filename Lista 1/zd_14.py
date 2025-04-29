from random import random

proby = 1
liczba = int(random() * 101)
poczatek = 0
koniec = 101
srodek = int((koniec - poczatek) / 2)
odp = 0
while True:
    print(f"Moj strzal to {srodek}")
    user = int(input("czy zgadlem: 1 tak 2 za duzo 3 za malo: "))

    if user == 1:
        break
    elif user == 2:
         temp = srodek
         srodek = int((srodek + poczatek) / 2)
         koniec = temp
    else:
        temp = srodek
        srodek = int((srodek + koniec) / 2)
        poczatek = temp
    proby += 1

print(f"Wygralem za {proby} razem")