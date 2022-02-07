# print() #str rezulta
# input() #str rezulta
# "".format() #str rezulta

# def functie2():
#     myfunction()
#
#
# def my_function():
#     # function body
#     return None #Functia nu este valida daca nu are function body. Putem evita asta folosind Return None sau Pass
#
# print(functie2())


# def message():
#     print("Enter a value")
#
# message()

#Namespaceul este locul in care anumite lucruri sunt declarate. Exista namespace local (al functiei) si namespace global.
# Functiile pot fi chemate in namespaceul unei functii chiar daca nu au fost definite

# def your_function(x: str) -> str:
#     print ("Hello", x)
#     return x

# name = input("Numele meu este: ")
# your_function(name)

#Testare data pentru CNP:
#
# # data='220227'
# import datetime
# # try:
# #
# #     return True
# # except ValueError:
# #     return False
#
# datetime.datetime.strptime('220227', '%y%m%d')
#
# a = "1920521228844"
#
# anul= a[2:4]
#
#
# print(anul)

# def my_function(a: str, b: str, c: str) ->:
#     return a, b, c

# print(my_function(a='2', c='3', b='2'))

# print(my_function('1','2','3'))

# print(my_function('1', c='2', b='3'))

# def my_function(n):
#     if n % 2 == 0:
#         return True
#     return False  #este bine sa returnam perechi de valori boolean
#
# print(my_function(4))
# print(my_function(3))
#
# nr = input("Introdu un nr: ")
# if my_function(int(nr)) is True:
#     print("Nr este divizibil cu 2")
# elif my_function(int(nr)) is False:
#     print("Nr nu este divizibil cu 2")


# def my_function():
#     return f"Cunosti aceasta variabila: {var}"
#
# var = 1
#
# print(my_function())  #In cazul asta var e si in namespaceul global, si este atribuit si in functie
# print(var)

# var = 1

# def my_function():
#     global var
#     var = 2
#     return f"Cunosti aceasta variabila: {var}"
#
# var = 1
# print(my_function())  #In cazul asta var e si in namespaceul global, si este atribuit si in functie
# print(var)

# lista = [1, 2, 3, [4, 5, [6, 7]]]
#
# print(lista[3][2][0])

# try:
#     # Bloc de expresii
# except:
#     # daca apare o exceptie si vrem sa afisam ceva

try:
    valoare = int(input("Prima cifra din CNP: "))
    # impartire = 1/valoare
    lista = [1]
    valoare = lista[0.5]
except TypeError:
    print("Eroare la tipul variabilei")
except AttributeError:
    print("Eroare de atribut")
except ValueError:
    print("Ai introdus o litra in loc de cifra")
except ZeroDivisionError:
    print("Eroare la impartire")
except Exception as e:
    print("Exceptie la impartire", e)