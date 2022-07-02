dane = [-10, -9, -7, -6, -4, -3, 0, 1, 3, 5, 10, 13, 18, 24]

def szukanie(val, tablica):
    for wartosc in tablica:
        if int(val) == wartosc:
            return True
    return False

szukana = input("Podaj szukaną wartość: ")

if szukanie(szukana, dane):
    print("Wartosc", szukana, "znajduje sie w tablicy")
else:
    print("Wartosc ", szukana, " nie znajduje sie w tablicy")


