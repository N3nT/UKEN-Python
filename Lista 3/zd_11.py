L = list(range(1,21))
text = "Ta kobieta byla jak moneta, szla z reki do reki, ale nie straciła na wartości."

liczby = {x for x in L if x % 3 == 0 or x % 5 == 0}
print(liczby)

words = text.split(sep=" ")
clean_words = []
for w in words:
    w_clean = w.lower().strip(",.")
    clean_words.append(w_clean)

dlugosci = {len(x) for x in clean_words}
print(dlugosci)

common = {x for x in liczby if x in dlugosci}
print(common)

if 42 not in common:
    common.add(42)

other_set = {1, 2, 3, 5, 10, 15, 20, 42}

is_subset = common.issubset(other_set)

print(common)
print(is_subset)