from collections import Counter

def make_eq(lista):
    return Counter(lista)


listaA = ["monety", "miecz", "miecz", "helm", "buty"]

ekwipunek = make_eq(listaA)

print(ekwipunek)

