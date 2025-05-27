import random

n = int(input("Podaj n z zakresu 2-100: "))

def single_simulation(n):
    urny = set()
    rzuty = 0

    while len(urny) < n:
        rzut = random.randint(0, n-1)
        urny.add(rzut)
        rzuty += 1

    return rzuty

def multiple_simulations(n, num_simulations):
    results = []
    for i in range(num_simulations):
        score = single_simulation(n)
        results.append(score)
    return results

def show_summary(results):
    total = sum(results)
    avg = total / len(results)

    print(f"srednia ilosc potrzebnych rzutow {avg}")


results = multiple_simulations(n, 10)
print(results)
show_summary(results)

