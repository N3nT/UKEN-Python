x = int(input("Podaj liczbe: "))

if x < 0:
    print("Liczba jest ujemna")
else:
    i = 1
    suma = 0
    while i <= x:
        suma += i
        i = i + 1
    print(suma)