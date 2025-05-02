lista = []
lista2 = []

## 1
for i in range(10):
    lista.append(i**2)

print(lista)

## 2
numbers = [-1, 2, -6, 9]
def kwadraty(numbers):
    for num in numbers:
        lista2.append(num**2)

    print(lista2)

kwadraty(numbers)