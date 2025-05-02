from random import choice

hangman = ["----", "|  |", "|  O", "| /\\", "| /\\"]
guessed_letters = []
words_list = ["dom", "mama", "tata", "pies"]
attempts = 0
game_status = False

def choose_word():
    word = choice(words_list)
    return word

def hide_letters(word):
    hidden = ""
    for letter in word:
        if letter in guessed_letters:
            hidden += letter
        else:
            hidden += "_"
    print(hidden)
    return hidden

def guess_letter(word, attempts):
    letter = input("Podaj litere: ")
    if letter in word:
        print("Zgadles litere")
        guessed_letters.append(letter)
    else:
        print("Nie zgadles litery")
        attempts += 1

    return attempts

def print_hangman(num):
    for i in range(num):
        print(hangman[i])

def check_win(hidden):
    if "_" in hidden:
        return False
    else:
        return True

word = choose_word()
while attempts < 5:
    attempts = guess_letter(word, attempts)
    hidden = hide_letters(word)
    if check_win(hidden):
        game_status = check_win(hidden)
        break
    print_hangman(attempts)

if game_status:
    print("Wygrales")
else:
    print(f"Przegrales, szukane slowo to: {word}")




