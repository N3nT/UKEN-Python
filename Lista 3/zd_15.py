import random

symbols = ["wisnie", "pomarancze", "sliwki", "dzwonki", "melony", "sztabki"]

def draw_symbols():
    results = []
    for i in range(3):
        results.append(random.choice(symbols))
    print(results)
    return results

def calculate_winnings(bet, symbols):
    set_symbols = set(symbols)
    winnings = 0
    if len(set_symbols) == 3:
        print("Przegrales")
        winnings = -bet
    elif len(set_symbols) == 2:
        print("Trafiles 2")
        winnings = bet*2
    else:
        print("Trafiles 3")
        winnings = bet*3

    return winnings

def play_round():
    try:
        bet = int(input("Wrzuc monete(0 aby wyjsc): "))
        if bet == 0:
            return None
        drawed = draw_symbols()
        win = calculate_winnings(bet, drawed)
        return win
    except ValueError:
        print("Podaj liczbe")

def main():
    print("---Jednoreki bandyta---")
    games = 0
    total = 0
    while True:
        result = play_round()
        if result is None:
            print(f"Koniec gry. Liczba rund: {games}, saldo: {total} zł")
            break
        total += result
        games += 1

main()

