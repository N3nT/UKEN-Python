from random import random

orly = 0
reszka = 0

for i in range(100):
    x = int(random() * 2)
    if x == 0:
        orly += 1
    else:
        reszka += 1

print(f"Orly: {orly}")
print(f"Reszki: {reszka}")