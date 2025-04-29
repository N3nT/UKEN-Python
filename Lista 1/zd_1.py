cena = int(input("Podaj wartosc zakupow: "))

if int(cena) > 100:
    rabat = cena * 0.8
    print("Rabat 20%")

else:
    rabat = cena * 0.9
    print("Rabat 10%")

print("Ostateczna cena: ", rabat)