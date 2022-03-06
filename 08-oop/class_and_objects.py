#O clasa reprezinta sablonul unui obiect. Obiectul reprezinta o instanta a clasei. Obiectul va avea propriile date dar comportamentul specific clasei

# class MyFirstClass:    #Denumirile de clasa incep cu litera mare. Daca clasa nu are nimic intre paranteze(), nu avem mosteniri de clase
#     pass
#
# #Adaugam un obiect
#
# my_first_object = MyFirstClass()

# class Caine:
#     nr_picioare = 4  #Nr picioare este un atribut al clasei Caine. Atributul este declarat la nivel de clasa
#     def __init__(self, name, age=3):   #Daca name nu are valoare default, acesta trebuie declarat neaparat cand se instanteaza clasa
#         self.nume = name
#         self.varsta = age
#
#
#     def __str__(self):   #Str exporta mereu un string
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name):  #Aceasta este o metoda specifica clasei
#         self.nume = name
#         return 'Ceva'

# print(Caine.nr_picioare)   #Chemare atribut din afara clasei

#Cea mai importanta metoda din cadrul unei clase este constructorul. Se foloseste __init__

# cainele_meu = Caine("Rex")
# # print(cainele_meu)
# # print(cainele_meu.nume)
#
# print(cainele_meu.change_name("Ben"))
# print(cainele_meu)
#
# print(cainele_meu.varsta)


class Calculator:

    def __init__(self, op1, op2, operation):    #Acestea sunt proprietatile obiectului
        self.operator1 = op1                    #Selful ne ajuta sa preluam valorile
        self.operator2 = op2
        self.operatie = operation

    def adunare(self):
        return self.operator1 + self.operator2

    def scadere(self):
        return self.operator1 - self.operator2

    def __str__(self):
        if self.operatie == '+':
            return f"{self.adunare()}"
        elif self.operatie == '-':
            return f"{self.scadere()}"

obiect1 = Calculator(1, 2, '+')
obiect2 = Calculator(1, 2, '-')
print(obiect1, obiect2)





