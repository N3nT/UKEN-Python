from collections import Counter
dict = {}
tab = []
tekst = "Could not find platform independent libraries <prefix>"

for letter in tekst:
    letter = letter.upper()
    if letter.isalpha():
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1

print(dict)

for letter in tekst:
    letter = letter.upper()
    if letter.isalpha():
        tab.append(letter)

licznik = Counter(tab)
print(licznik)