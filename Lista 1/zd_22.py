dunbar = 150
n = 5
tygodnie = 1
while n <= 150:
    print(f"W {tygodnie} tygodniu profesor ma {n} znajomych")
    n -= tygodnie
    n *= 2
    tygodnie += 1
print(f"W {tygodnie} tygodniu profesor ma {n} znajomych")
