#1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorilesunt egale, returnati de trei ori suma acestora.(1 punct)

def suma_de_trei_nr(*args):
    lista = [*args]
    if len(lista) != 3:
        print("Ati introdus mai mult de 3 argumente pentru functie. Va rog introduceti doar 3 numere in paranteze, separate de virgule")
        return None
    else:
        if lista[0] == lista[1] == lista[2]:
            return 9*(lista[0])
        else:
            return lista[0]+lista[1]+lista[2]


print(suma_de_trei_nr(1, 6, 9))
print(suma_de_trei_nr(5, 5, 5))
print(suma_de_trei_nr(1, 6, 9,12))

# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_trimmer(list):
    if len(list)>=3:
        list_to_pop=[]
        x = len(list)
        for i in range(len(list)):
            if (i+1)%3 == 0 and i<=len(list)-1:
                list_to_pop.append(list[i])  #salvam intai toate numerele din lista care trebuie scoase
        for j in list_to_pop:
            print(j)
            list.remove(j)                   #apoi le scoatem din lista originala
        return list
    elif len(list) == 2:
        print(list[1])
        list.pop(1)
        print(list[0])
        list.pop(0)
        return list
    elif len(list) == 1:
        print(list[0])
        list.pop(0)
        return list

def loop_trimmer(list):
    while len(list)>0:
        list_trimmer(list)
    return None

loop_trimmer(lista)



