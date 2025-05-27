import random

def generate_random_grid(n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

def find_fours(grid):
    n = len(grid)
    matches = set()

    def check_direction(dx, dy):
        for i in range(n):
            for j in range(n):
                if 0 <= i + 3*dx < n and 0 <= j + 3*dy < n:
                    val = grid[i][j]
                    if all(grid[i + k*dx][j + k*dy] == val for k in range(4)):
                        for k in range(4):
                            matches.add((i + k*dx, j + k*dy))

    # kierunki: poziomo, pionowo, ukośnie ↘ i ↙
    for dx, dy in [(0,1), (1,0), (1,1), (1,-1)]:
        check_direction(dx, dy)

    return matches

def display_grid(grid, matches):
    for i, row in enumerate(grid):
        line = ""
        for j, val in enumerate(row):
            if (i, j) in matches:
                line += f"*{val}* "
            else:
                line += f" {val}  "
        print(line)
    print()

def simulation():
    while True:
        try:
            n = int(input("Podaj rozmiar planszy (10–20): "))
            if not (10 <= n <= 20):
                print("Podaj liczbę z zakresu 10–20.")
                continue
        except ValueError:
            print("To nie liczba!")
            continue

        grid = generate_random_grid(n)
        matches = find_fours(grid)
        display_grid(grid, matches)

        again = input("Czy chcesz wykonać kolejną symulację? (t/n): ")
        if again.lower() != 't':
            break

simulation()
