from random import random

def throw():
    one = int(random() * 6) + 1
    two = int(random() * 6) + 1

    return one + two

def single_game():
    score = throw()
    print(f"Wyrzuciles {score}")
    if score == 7 or score == 11:
        print("Wygrales")
        return True
    elif score == 2 or score == 3 or score == 12:
        print("Przegrales")
        return False
    else:
        print("Grasz dalej")
        score = throw()
        print(f"Wyrzuciles {score}")
        if score == 7 or score == 2 or score == 3 or score == 12:
            print("Przegrales")
            return False
        else:
            print("Wygrales")
            return True

def get_answer():
    answer = input("Czy chcesz kontynuowac gre (tak/nie): ")
    if answer == "tak":
        return True
    else:
        return False

def game():
    gameStatus = True
    win = 0
    lose = 0
    while gameStatus:
        score = single_game()
        if score:
            win += 1
        else:
            lose += 1
        gameStatus = get_answer()

    print(f"Wygrales {win} razy")
    print(f"Przegrales {lose} razy")

game()