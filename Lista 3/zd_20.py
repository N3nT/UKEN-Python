import random

def single_game(seq1, seq2):
    """Przeprowadza jedną grę i zwraca (zwycięzca, liczba_rzutów)"""
    history = ""
    toss_count = 0
    while True:
        history += random.choice(['O', 'R'])
        toss_count += 1
        if len(history) >= len(seq1):
            if history[-len(seq1):] == seq1:
                return 1, toss_count
            elif history[-len(seq2):] == seq2:
                return 2, toss_count

def simulate_games(seq1, seq2, num_games=1000):
    """Symuluje wiele gier i zlicza zwycięstwa"""
    wins = {1: 0, 2: 0}
    for _ in range(num_games):
        winner, _ = single_game(seq1, seq2)
        wins[winner] += 1
    return wins

def show_results(pair_name, seq1, seq2, results):
    """Wyświetla zestawienie wyników"""
    print(f"\n=== Wyniki dla {pair_name} ===")
    print(f"Gracz 1 ({seq1}): {results[1]} zwycięstw")
    print(f"Gracz 2 ({seq2}): {results[2]} zwycięstw")

def main():
    pairs = [
        ("Para 1", "OORO", "OROO"),
        ("Para 2", "OROO", "ROOO"),
        ("Para 3", "ROOO", "OORO"),
    ]

    for name, seq1, seq2 in pairs:
        results = simulate_games(seq1, seq2)
        show_results(name, seq1, seq2, results)

main()
