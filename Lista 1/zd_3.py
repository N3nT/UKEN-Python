plec = input("Podaj plec (M - mezczyzna, K - kobieta): ")

if plec == "K":
    wiek = int(input("Podaj wiek: "))
    if wiek >= 10 and wiek <= 13:
        print("Mozesz zagrac w zespole")
    else:
        print("Nie mozesz zagrac w zespole")
else:
    print("Nie mozesz zagrac w zespole")