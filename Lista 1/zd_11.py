n = int(input("Podaj liczbe n > 2: "))
k = int(input("Podaj liczbe k < n: "))

for i in range(n):
    if i % 2 == 0:
        continue
    else:
        print(i)