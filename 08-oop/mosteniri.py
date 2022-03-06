# 1. Vehicul - clasa principala sau superclasa pentru 1.1-1.4
# 1.1 Vehicul de apa -subclasa pt 1
# 1.2 Vehicul de aer -subclasa pt 1
# 1.3 Vehicul de spatiu -subclasa pt 1
# 1.4 Vehicul terestru - subclasa pt 1
# 1.4.1 Vehicul de teren -subclasa pt 1.4
# 1.4.2 Vehicul de curse -subclasa pt 1.4

# 2. Animale
# 2.1 Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2 Reptile
# 2 este superclasa pentru 2.1 si 2.2
# 2.1 si 2.2 sub subclase pt 2
# 2.1.1 si 2.1.2 pentru 2.1 sunt subclase
# 2.1.1 si 2.1.2 pentru 2 sunt tot subclase, chiar daca nu sunt direct mostenite

# Max este un caine mare care doarme toata ziua.
# Obiectul -> Max (substantiv)
# Clasa    -> Caine (substantiv)
# Proprietatea -> mare (adjectiv)
# Activitatea  -> doarme toata ziua (verb) (poate sa fie transformat intr-o metoda)

# Un Logan verde merge incet.
# Obiectul -> Un Logan
# Clasa    -> Masina
# Proprietatea -> Verde
# Activitate -> merge incet

# Rudolph este o pisica mare care mananca multe boabe
# Obiectul -> Rudolph
# Clasa    -> Pisica
# Proprietatea -> Mare
# Activitate -> Mananca multa boabe

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online
# Obiectul -> Lenovo
# Clasa    -> calculator/laptop
# Proprietatea -> gri
# Activitate -> se poate cumpara

# Sa se realizeze jocul x si 0 intre 2 jucatori, in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiectele -> calculatorul/omul
# clasa -> Regula
# proprietate -> Mutarile / calculul de scor al jocului

# class MyFirstClass:
#     pass
#
# my_object = MyFirstClass()

# stack = []
#
# def push(val):
#     stack.append(val)
#     return stack
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())

# class Stack:
#     def __init__(self):
#         self.__stack_list = []  #Daca folosim __, proprietatea devine privata, nu mai poate fi accesata
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):
#         return f"{self.__stack_list}"
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
#
# print(obiect_stiva)
#
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())

# class ClasaExemplu:
#     def __init__(self, val = 1):
#         self.first = val
#         self.second = 0
#
#     def set_second(self, val = 2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
# obiect_3 = ClasaExemplu(3)
#
# print(obiect_1)
# print(obiect_2)
# print(obiect_3.set_second(8))
# print(obiect_3)


# class Caine:
#     nr_picioare = 4  #Nr picioare este un atribut al clasei Caine. Atributul este declarat la nivel de clasa
#     def __init__(self, name, vaccin, age=3):   #Daca name nu are valoare default, acesta trebuie declarat neaparat cand se instanteaza clasa
#         self.__nume = name
#         self.__varsta = age
#         self.__vaccinuri = vaccin
#         # Caine.nr_picioare = 3
#         self.stare = 'tanar'
#         self.cumpara = 'nimic'
#         if self.__varsta == 4:   #In constructor are trebui sa se puna doar valori default de obicei
#             self.stare = 'batran'
#         else:
#             self.cumpara = 'jucaria'
#
#
#     def __str__(self):   #Str exporta mereu un string
#         return f"{self.__nume} - {self.__varsta}"
#
#     def change_name(self, name):  #Aceasta este o metoda specifica clasei
#         self.__nume = name
#         return 'Ceva'
#
# obiect_1 = Caine('Rex', age=4, vaccin=10)
# print(obiect_1.__dict__)     #Aceasta instantiere ne afiseaza care sunt proprietatile!
# print(Caine.__dict__)     #Aceasta instantiere ne afiseaza care sunt proprietatile!
# # print(obiect_1._Caine__nume)   #In felul asta accesam proprietati private
# # print(obiect_1.nr_picioare, 'nr picioare')
# # print(obiect_1.varsta, 'varsta')
# # print(obiect_1.nume, 'nume')
# # print(obiect_1.vaccinuri, 'vaccin')
#
# print(hasattr(Caine, 'nr_picioare'))
# print(type(obiect_1).__name__)


class Validator:
    def __init__(self, cnp):
        self.CNP = cnp

    def lungime(self):
        if len(self.CNP) !=13:
            return False
        return True


    def __str__(self):
        if self.lungime() is True:
            return f"CNPul {self.CNP} este valid"
        else:
            return f"CNPul {self.CNP} nu este valid"



obiect_1 = Validator(input("Introdu cnpul: "))
print(obiect_1)




