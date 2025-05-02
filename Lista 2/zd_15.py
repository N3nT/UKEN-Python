from random import random

word_list = ['Python', 'Java', 'JavaScript']

def choose_word(word_list):
    index = int(random() * len(word_list))
    return word_list[index]

def check_letter(word, letter):
    if letter in word:
        print("Tak")
    else:
        print("Nie")

def play_game(word_list):
    word = choose_word(word_list)
    proby = 5
    print(f"Slowo zawiera {len(word)} liter")

    while proby != 0:
        print(f"Pozostale proby {proby}")
        letter = input("Zgadnij litere: ")
        check_letter(word, letter)
        proby -= 1

    answer = input("Zgadnij slowo: ")
    if answer == word:
        print("Wygrales")
    else:
        print("Przegrales")

play_game(word_list)