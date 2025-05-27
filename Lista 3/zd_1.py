import random
import string

# a)
L = [i for i in range(0, 100)]
print(L)

# b)
kwadraty = [i**2 for i in L]
print(kwadraty)

# c)
parzyste = [i for i in L if i%2==0]
print(parzyste)

# d)
binarne = [bin(i)[2:] for i in L]
print(binarne)

# e)
przedial = [i for i in L if 20 <= i <= 50]
print(przedial)

# f)
S1 = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 30)))for _ in range(20)]
print(S1)

# g)
samogloski = ['a', 'e', 'i', 'o', 'u']
bezsamoglosek = [text for text in S1 if not any(char in samogloski for char in text)]
print(bezsamoglosek)

# h)
chars = string.ascii_lowercase + string.digits
S2 = [''.join(random.choices(chars, k=random.randint(3, 30)))for _ in range(20)]
print(S2)

# i)
S2_bez_cyfr = [''.join(char for char in s if char not in string.digits) for s in S2]
print(S2_bez_cyfr)

# j)
S2_bez_liter = [
    int(''.join(char for char in s if char not in string.ascii_lowercase))
    for s in S2 if ''.join(char for char in s if char not in string.ascii_lowercase) != ''
]
print(S2_bez_liter)

# k)
K = [tuple(random.randint(0, 100) for _ in range(random.randint(1, 6))) for _ in range(20)]
print(K)

# l)
dwa_el = [K[:2] for k in K if len(k) >= 2]
print(dwa_el)

# m)
nieparzysta_sum = [k for k in K if sum(k) % 2 != 0]
print(nieparzysta_sum)

# n)
podziel_przez_3 = [k for k in K if all(x % 3 == 0 for x in k)]
print(podziel_przez_3)

# o)
jest_podziel_przez_3 = [k for k in K if any(x % 3 == 0 for x in k)]
print(jest_podziel_przez_3)
