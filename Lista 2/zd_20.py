import random

# Początkowe listy
przymiotniki = ["głupi", "niezdarny"]
rzeczowniki = ["burak", "gamoniu"]

def przymiotnik_wiekowy(wiek):
    if wiek < 18:
        return "nieopierzony"
    elif wiek < 50:
        return "naiwny"
    else:
        return "zgrzybiały"

def dodaj_slowo(lista, typ):
    if typ == "przymiotnik":
        slowo = input("Podaj przymiotnik do dodania: ")
        lista.append(slowo)
    else:
        slowo = input("Podaj rzeczownik do dodania: ")
        lista.append(slowo)

def usun_slowo(lista, typ):
    if len(lista) <= 2:
        print(f"Muszą pozostać przynajmniej 2 {typ}i!")
        return
    print(f"Aktualne {typ}i:", lista)
    slowo = input(f"Podaj {typ} do usunięcia: ")
    if slowo in lista:
        lista.remove(slowo)
    else:
        print(f"{typ.capitalize()} '{slowo}' nie znaleziony.")

def generuj_obelge(imie, wiek):
    p1 = random.choice(przymiotniki)
    p2 = przymiotnik_wiekowy(wiek)
    r = random.choice(rzeczowniki)
    print(f"\n{imie}, ty {p2}, {p1} {r}!\n")

def menu():
    print("=== Generator Obelg ===")
    print("1. Dodaj przymiotnik")
    print("2. Usuń przymiotnik")
    print("3. Dodaj rzeczownik")
    print("4. Usuń rzeczownik")
    print("5. Wygeneruj obelgę")
    print("6. Zakończ")

# Program główny
def main():
    while True:
        menu()
        try:
            wybor = int(input("Wybierz opcję: "))
        except ValueError:
            print("Podaj poprawny numer.")
            continue

        if wybor == 1:
            dodaj_slowo(przymiotniki, "przymiotnik")
        elif wybor == 2:
            usun_slowo(przymiotniki, "przymiotnik")
        elif wybor == 3:
            dodaj_slowo(rzeczowniki, "rzeczownik")
        elif wybor == 4:
            usun_slowo(rzeczowniki, "rzeczownik")
        elif wybor == 5:
            imie = input("Podaj imię osoby: ")
            try:
                wiek = int(input("Podaj wiek osoby: "))
            except ValueError:
                print("Wiek musi być liczbą!")
                continue
            generuj_obelge(imie, wiek)
        elif wybor == 6:
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
