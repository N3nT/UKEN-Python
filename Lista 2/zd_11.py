text = input("Podaj tekst: ")

samogloski = 'aeiouyAEIOUY'
wynik = ""

for letter in text:
    if letter not in samogloski:
        wynik += letter

print(wynik)