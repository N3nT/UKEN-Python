from random import random

proby = 1
liczba = int(random() * 101)
odp = 0
while odp != liczba:
    odp = int(input("Podaj liczbe:"))
    if odp == liczba:
        break
    elif odp < liczba:
        print("Za malo")
    else:
        print("Za duzo")
    proby += 1

print(f"Wygrales za {proby} razem")