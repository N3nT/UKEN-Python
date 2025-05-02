text = input("Podaj tekst: ")

litery = {}

for letter in text:
    if letter in litery:
        litery[letter] += 1
    else:
        litery[letter] = 1

print(litery)