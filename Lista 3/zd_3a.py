def transponuj_lista_skladana(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def transponuj_petle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    return transposed

def wyswietl_macierz(macierz):
    for wiersz in macierz:
        print('\t'.join(map(str, wiersz)))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Macierz oryginalna:")
wyswietl_macierz(matrix)

print("\nTransponowana (list comprehension):")
macierz_transponowana_1 = transponuj_lista_skladana(matrix)
wyswietl_macierz(macierz_transponowana_1)

print("\nTransponowana (pętle):")
macierz_transponowana_2 = transponuj_petle(matrix)
wyswietl_macierz(macierz_transponowana_2)
