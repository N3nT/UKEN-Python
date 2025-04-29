wiersze = int(input("Podaj liczbe wierszy: "))

for i in range(wiersze):
    gwiazdki = 2 * i + 1
    spacje = wiersze - i - 1

    for j in range(spacje):
        print(" ", end="")
    for j in range(gwiazdki):
        print("*", end="")

    print("")