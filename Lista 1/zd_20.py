n = int(input("Podaj liczbę wyrazów: "))

suma_dodatnia = 0.0
suma_naprzemienna = 0.0

for i in range(2, n + 1):
    znak = (-1) ** i
    suma_dodatnia += 1.0 / i
    suma_naprzemienna += znak * (1.0 / i)

print(f"Suma ciągu dodatniego: {suma_dodatnia}")
print(f"Suma ciągu naprzemiennego: {suma_naprzemienna}")
