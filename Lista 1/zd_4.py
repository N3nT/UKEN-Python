rok = int(input("Podaj rok: "))

if rok % 4 == 0:
    if rok % 100 == 0:
        if rok % 400 == 0:
            print("Rok jest przestepny")
        else:
            print("Rok nie jest przestepny")
    else:
        print("Rok przestepny")
else:
    print("Rok jest nie przestepny")