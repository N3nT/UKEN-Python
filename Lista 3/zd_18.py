import random
import time
import os


def random_grid(n):
    return [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]


def display(grid):
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print(" ".join("■" if cell == 1 else "o" for cell in row))
    print()


def count_neighbors(grid, row, col):
    n = len(grid)
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = (row + dr) % n
            c = (col + dc) % n
            count += grid[r][c]
    return count


def next_generation(grid):
    n = len(grid)
    new_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors in [2, 3]:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid


def main():
    print("--- Gra w życie ---")
    try:
        n = int(input("Podaj rozmiar planszy (np. 10–30): "))
        steps = int(input("Podaj liczbę pokoleń do pokazania: "))
    except ValueError:
        print("Błędna wartość. Podaj liczby całkowite.")
        return

    grid = random_grid(n)

    for _ in range(steps):
        display(grid)
        time.sleep(0.5)
        grid = next_generation(grid)


main()
