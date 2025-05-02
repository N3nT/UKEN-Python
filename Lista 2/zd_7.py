def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number // 2
    else:
        print(number * 3 + 1)
        return 3 * number + 1

n = int(input("Podaj liczbe: "))

while n > 1:
    n = collatz(n)