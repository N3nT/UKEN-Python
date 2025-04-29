dni = int(input("Podaj liczbe dni w miesiacu: "))
pocz = int(input("Podaj poczatkowy dzien miesiaca (1-pon, 7-nie): "))

for i in range(pocz - 1):
    print("   ", end="")

for i in range(1, dni + 1):
    print(f"{i:3}", end="")

    if (i + pocz - 1) % 7 == 0:
        print(" ")