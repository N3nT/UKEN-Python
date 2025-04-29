wiatr = int(input("Podaj preskosc wiatru w wezlach: "))

if wiatr < 1:
    print("Cisza")
elif wiatr >= 1 and wiatr <= 3:
    print("Zefir")
elif wiatr >= 4 and wiatr <= 27:
    print("Bryza")
elif wiatr >= 28 and wiatr <= 47:
    print("Wichura")
elif wiatr >= 48 and wiatr <= 63:
    print("Sztorm")
else:
    print("Huragan")