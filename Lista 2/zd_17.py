L = []

L.insert(2, -1)
print(L)

# L[2] = -1
# print(L)

#Jezeli nie lista ma mniejszy rozmiar to insert doda wartosc w pierwsze wolne, przypisanie spowoduje blad

L.insert(0, 2)
L.insert(len(L), 3)

print(L)