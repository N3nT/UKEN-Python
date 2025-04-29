punkty = int(input("Podaj ilosc punktow: "))

if punkty <= 100 and punkty >= 90:
    print("Ocena A")
elif punkty < 90 and punkty >= 80:
    print("Ocena B")
elif punkty < 80 and punkty >= 70:
    print("Ocena C")
elif punkty < 70 and punkty >= 60:
    print("Ocena D")
elif punkty < 60 and punkty >= 0:
    print("Ocena E")
else:
    print("Podano bleda ilosc punktow")