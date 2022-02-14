#Map are rolul de a modifica fiecare element al unei liste

# def adunare(n):
#     return n+n
#
# lista_numere = [1, 2, 3, 4]
#
# rezultat = map(adunare, lista_numere)
#
# print(list(rezultat))


# lista_numere = [1, 2, 3, 4]
#
# rezultat = map(lambda n: n+n, lista_numere)  #Functia de mai sus se poate schimba cu o functie lambda simpla
#
# print(list(rezultat))

lista_numere = [1, 2, 3, 4, 6]
lista_numere_2 = [5, 6, 7, 8]


rezultat = map(lambda n, m: n+m, lista_numere, lista_numere_2)

print(list(rezultat))

def adunare_liste(a, b):
    suma = 0
    lista_adunare = []
    for i, v in enumerate(lista_numere):
        for j, w in enumerate(lista_numere_2):
            if i==j:
                suma = v+w
                lista_adunare.append(suma)
    return lista_adunare

print(adunare_liste(lista_numere, lista_numere_2))