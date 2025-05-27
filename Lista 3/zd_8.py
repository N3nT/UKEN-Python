tekst1 = input("Podaj napis 1: ")
tekst2 = input("Podaj napis 2: ")

zbior1 = set(tekst1)
zbior2 = set(tekst2)

allLetter = zbior1 | zbior2
onlyOne = zbior1 - zbior2
onlyTwo = zbior2 - zbior1
common = zbior1 & zbior2

print(allLetter)
print(onlyOne)
print(onlyTwo)
print(common)