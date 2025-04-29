flaga = True
while flaga:
    x = int(input("Podaj liczbe calkowita n > 0: "))
    if x > 0:
        flaga = False
    else:
        print("Podales zla liczbe")

    i = 0
    suma = 0
    while i <= x:
        suma += i**2
        i += 1

    print(suma)