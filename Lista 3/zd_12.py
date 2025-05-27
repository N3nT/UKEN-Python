text1 = "Python to jezyk programowania. Python to jezyk obiektowy."
text2 = "Programowanie w jezyku Python jest bardzo popularne. Python jest jezykiem interpretowanym."

clean_words1 = []
words1 = text1.split(sep=" ")
for w in words1:
    w_clean = w.lower().strip(",.")
    clean_words1.append(w_clean)

clean_words2 = []
words2 = text2.split(sep=" ")
for w in words2:
    w_clean = w.lower().strip(",.")
    clean_words2.append(w_clean)

print(clean_words1)
print(clean_words2)

unikalne = set(clean_words1)
unikalne.update(clean_words2)

print(unikalne)

wspolne = set(clean_words1) & set(clean_words2)
print(wspolne)

jeden = set(clean_words1) - set(clean_words2)
print(jeden)

dlugosci = {len(x) for x in wspolne}
print(dlugosci)