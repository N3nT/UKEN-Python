zero_bezwgledne = -273.15

def convert(celsjusze):
    faren = 9/5 * celsjusze + 32
    return faren

x = 0
while x > zero_bezwgledne:
    x = float(input("Podaj celsjusze: "))
    print(convert(x))