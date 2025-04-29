from random import random

tab = [0,0,0,0,0,0]

for i in range(1000):
    x = int(random() * 6)
    if x == 0:
        tab[0] += 1
    elif x == 1:
        tab[1] += 1
    elif x == 2:
        tab[2] += 1
    elif x == 3:
        tab[3] += 1
    elif x == 4:
        tab[4] += 1
    elif x == 5:
        tab[5] += 1

print(tab)