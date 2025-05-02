scores = []

def show_menu():
    print("### Menu ###")
    print("1. Dodaj nowy wynik")
    print("2. Usun wynik")
    print("3. Sortuj wyniki")
    print("4. Wyswietl wyniki")
    print("5. Zakoncz program")

def add_score(scores):
    score = int(input("Wynik: "))
    scores.append(score)
    scores.sort(reverse=True)

    if len(scores) > 5:
        print(f"Usunieto wynik {scores.pop()}")

def delete_score():
    wynik = int(input("Wynik do usuniecia: "))
    scores.remove(wynik)

if __name__ == '__main__':
    while True:
        show_menu()
        answer = int(input("Wybierz opcje: "))

        if answer == 1:
            add_score(scores)
        elif answer == 2:
            delete_score()
        elif answer == 3:
           scores.sort(reverse=True)
        elif answer == 4:
            print(scores)
        elif answer == 5:
            exit()
