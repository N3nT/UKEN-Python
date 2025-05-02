def srednia(a, b, c, d):
    wynik = a + b + c + d - min(a, b, c, d)
    return wynik / 3

print(srednia(1, 2, 3, 4))