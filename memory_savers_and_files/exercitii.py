# def function(new_list: list):
#     length = len(new_list)
#     temp_list = new_list[-1]
#     new_list[0] = new_list[length-1]
#     new_list[length - 1] = temp_list
#     return new_list
#
# param_list = [22, 11, 9, 44, 56]
# print(function(param_list))

#________________________________________________________

# a = "Ana are mere"
# lista=[]
# for i, e in enumerate(list(a)):
#     if i%2 == 0:
#         lista.append(e)
# print(lista)

#________________________________________________________

# lista = ['a', 'b', '12', 'cde']
# def functie(lista:list):
#     lista = [1, 2, 'abc']   #variabila de aici inlocuieste variabila glabala
#     new_list = []
#     for i in lista:
#         new_list.append(i)
#     return new_lst
#
# print(functie(lista))  #se va printa lista din functie

#________________________________________________________

# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]    #Cand se intalneste return, se iese din functie. Deci se va face doar lista[y+1] = lista[2] = 3
#
# lista = [1, 2, 3]
# print(functie(lista))

#________________________________________________________
#________________________________________________________
#________________________________________________________

# List comprehension, modalitatea de a scrie un for intr-un singur rand, folosind outputul de lista

#Lucrul de mai jos poate fi scris asa:

# lista = []
# for item in 'Ana are mere':
#     lista.append(item)
# print(lista)

#sau asa

# lista = [item for item in 'Ana are mere']   #itemul din stanga este ce se appenduiteste
# print(lista)

#________________________________________________________
#________________________________________________________

#Asa
a = "Ana are mere"
# lista=[]
# for i, e in enumerate(list(a)):
#     if i%2 == 0:
#         lista.append(e)
# print(lista)

#sau asa

# lista =[e for i, e in enumerate(list(a)) if i%2==0]
# print(lista)

#________________________________________________________
#________________________________________________________
#Alt exercitiu, scris direct cu instructiune pe o linie

# my_numbers = [1, 2, 3, 4, 5]
# lista_numere = [item ** 2 for item in my_numbers if item % 2 == 0]
# print(lista_numere)

#________________________________________________________
#________________________________________________________

#Alt exercitiu, scris direct cu instructiune pe o linie
# lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x for x in lista_produse if "a" in x]
# print(lista_noua)

#________________________________________________________
#________________________________________________________

#Alt exercitiu, scris direct cu instructiune pe o linie
# lista = [x for x in range(10) if x < 5]
# print(lista)

#________________________________________________________
#________________________________________________________
#________________________________________________________


# a, b = 10, 20  #Se pot declara mai multe variabile intr-o singura linie
# # min = a if a < b else b
# #Asa
# # if a < b:
# #     min = a
# # else:
# #     min = b
#
# #Sau asa
# min = a if a < b else b  #Ce e in stanga ifului se executa daca iful este adevarat
#
# print(min)

#________________________________________________________
#________________________________________________________
#Alt exercitiu, scris direct cu instructiune pe o linie
# lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x if x!='suc' else 'apa' for x in lista_produse]  #se executa forul intai, apoi iful. If-else trebuie mereu pus in stanga. Daca e if simplu, poate fi pus si dupa for.

#________________________________________________________
#________________________________________________________
#_________________FUNCTIA FILTER_________________________
#________________________________________________________
#________________________________________________________

# lista_numere = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]
#
# def functie_nr_pare(number):
#     if number % 2 == 0:
#         return True
#     return False
#
# iterator_numere_pare = filter(functie_nr_pare, lista_numere)
#
# print(list(iterator_numere_pare))

#________________________________________________________
#________________________________________________________
#
# litere = ['a', 'b', 'c', 'd', 'e', 'i', 'j']
# def filter_vocale(letter):
#     vocale = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vocale else False
#
# filtrare_vocale = filter(filter_vocale, litere)
# print(list(filtrare_vocale))

#________________________________________________________
#________________________________________________________
#
# x = 1
# def f():
#     return x   #Atunci cand x-ul nu este gasit in functie, este cautat in namespace-ul global
#
# print(x)
# print(f())

#________________________________________________________
#
# x = [1, 2, 'hello', 'world', ['another', 'list']]
#
# print(len(x[3]))

#________________________________________________________
# x = (1, 2, 3)
# x[1] = 4   #Tuplurile nu se pot modifica pe index
#
# print(x)

#________________________________________________________
# a = [1, 2, 3]
# b = [4, 5]
#
# print (a + b * 3)  #Se repeta elementele, nu se inmultesc matemate. Se appenduiesc repetat listele

#________________________________________________________
# x = [1, 2, 3, 4]
# print(x[-1:])  #va printa doar ultimul element

#________________________________________________________
# x = [1, 2, 3, 4]
# x= [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

#________________________________________________________
# # x = [1, 2, 3, 4]
# def exercitiu(i):
#     for i in range(i):
#         return i
# x = exercitiu(3)
#
# print(x)

#________________________________________________________

# def func(*args):
#     return 3+ len(args)
#
# print(func(4, 4, 4))







