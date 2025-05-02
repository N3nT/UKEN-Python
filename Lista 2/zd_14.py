from random import random, shuffle

word_list = ['Python', 'Java', 'JavaScript']

def choose_word(word_list):
    index = int(random() * len(word_list))
    return word_list[index]

def shuffle_word(word):
    letters = list(word)
    shuffle(letters)
    return ''.join(letters)

def play_game(word_list):
    word = choose_word(word_list)
    shuffled_word = shuffle_word(word)

    print(f"Co to za slowo: {shuffled_word}")

    while True:
        answer = input("Odpowiedz: ")
        if answer == word:
            print("Zgadles")
            break
        else:
            print("Nie zgadles sproboj ponownie")

play_game(word_list)