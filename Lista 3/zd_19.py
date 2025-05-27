import random

def single_simulation(n):
    """Zwraca numer pojemnika, do którego trafi kulka"""
    position = 0
    for _ in range(n):
        if random.choice([True, False]):
            position += 1  # w prawo
        # w lewo = nie zmieniamy pozycji
    return position

def run_simulations(n, trials):
    """Zwraca listę zliczającą ile kulek wpadło do danego pojemnika"""
    results = [0] * (n + 1)  # od 0 do n pojemników
    for _ in range(trials):
        bin_index = single_simulation(n)
        results[bin_index] += 1
    return results

def show_results(results):
    """Wyświetla tekstowy histogram"""
    print("\n--- Wyniki symulacji ---")
    for i, count in enumerate(results):
        print(f"Pojemnik {i:2d}: {'*' * count}")

def main():
    print("--- Deska Galtona ---")
    try:
        n = int(input("Podaj liczbę rzędów kołków (1–12): "))
        trials = int(input("Podaj liczbę kulek (np. 100): "))
        if not (1 <= n <= 12):
            print("Liczba rzędów musi być w zakresie 1–12.")
            return
    except ValueError:
        print("Podaj poprawne liczby całkowite.")
        return

    results = run_simulations(n, trials)
    show_results(results)

main()
