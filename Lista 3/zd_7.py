from collections import Counter

tekst = input("Podaj napis:")
list = []

for letter in tekst:
    list.append(letter)

odp = Counter(list)
print(odp)
