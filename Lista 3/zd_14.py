import random

answers = [
"Nie sadze.",
"Oczywiście, że tak!",
"Nie wiem.",
"Zapytaj ponownie później.",
"Na pewno nie!",
"Jest to prawdopodobne.",
"Wszystko wskazuje na tak.",
"Możliwe.",
"Watpliwe.",
"Bez watpienia!",
"Nie licz na to.",
"To pewne!"
]

def get_random_answer(answers):
    return random.choice(answers)

def play_game(answers):
    user = ''
    while user != "koniec":
        user = input("Zadaj pytanie: ")
        if user == "koniec":
            break

        print(get_random_answer(answers))


play_game(answers)