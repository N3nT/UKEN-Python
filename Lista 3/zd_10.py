text = "Trzeba byc zawsze tylko soba. Kon bez ulana jest zawsze koniem. Ulan bez konia tylko czlowiekiem."
words = text.split(sep=" ")

slowa = {word: {'count': words.count(word), 'length': len(word)} for word in set(words)}
print(slowa)

slowa_two = {k: v for k, v in slowa.items() if not (v['count'] == 1 and v['length'] < 5)}
print(slowa_two)

slowa_three = dict(sorted(slowa_two.items(), key=lambda x: x[1]['length'], reverse=True))
print(slowa_three)