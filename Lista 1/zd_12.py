def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while True:
    x = int(input("Podaj liczbe (-1 = koniec programu): "))
    if x == -1:
        break
    else:
        odp = czy_pierwsza(x)
        if odp:
            print("{:d} jest liczba pierwsza".format(x))
        else:
            print("{:d} nie jest liczba pierwsza".format(x))