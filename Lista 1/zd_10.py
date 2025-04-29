print("Witaj w systemie logowania komputera")

while True:
    haslo = input("Podaj haslo dostepu: ")

    if(haslo == "programowanie"):
        print("Logowanie zakonczylo sie sukcesem")
        break
    else:
        print("Bledne haslo! Odmowa dostepu!")