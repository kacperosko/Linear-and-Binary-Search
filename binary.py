dane = [-30, -25, -10, -9, -7, -6, -4, -3, -1, 0, 1, 2, 3, 5, 10, 11, 13, 15, 16, 18, 24]


def szukanie(tablica, val):
    lewo = 0
    prawo = len(tablica)
    indkes = 0

    while lewo < prawo:
        indkes = (lewo + prawo) // 2

        if tablica[indkes] == val:
            return "Indekds wynosi " + str(indkes)
        else:
            if tablica[indkes] < val:
                lewo = indkes + 1
            else:
                prawo = indkes

    return "Brak wartosci w tablicy"


szukana = int(input("Podaj szukana wartosc: "))

print (szukanie(dane, szukana))