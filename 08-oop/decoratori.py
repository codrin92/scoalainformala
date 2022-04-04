# #Un decorator este o functie care este folosita ca argument la alta functie
#
# # def decorator_simplu(parametru):
# #     print(f"Apelam functia {parametru.__name__}")
# #     return parametru
# #
# # @decorator_simplu
# # def functie_simpla():
# #     return "Buna seara"
# #
# # print(functie_simpla())
#
# def decorator_deposit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*args):
#             print(f"Ambalam produse din {functia_noastra.__name__} cu {material}")
#             return f'Ambalam produse din {functia_noastra.__name__} {", ".join(x for x in functia_noastra(*args))}'
#         return ambalaj_intern
#     return ambalaj
#
# @decorator_deposit("hartie")
# def impachetare_carti(*args):
#     return f"Impachetam carti: {args}"
#
# @decorator_deposit("folie_alimentara")
# def impachetare_fructe(*args):
#     return args
#
# print(impachetare_fructe("mere", "pere"))
#
# # a=impachetare_carti("Amintiri din copilarie", "Baltagul")
# # print(a)

# def decorator(functie):
#     def decoreaza(var):
#         return functie(var)
#     return decoreaza
#
# def p(functie):
#     def decoreaza(var):
#         return f"<p>{functie(var)}</p>"
#     return decoreaza
#
# @p
# def text(sir):
#     return sir.upper()

# text_p = decorator(text)
# print(text("Salut"))

# class Dog:
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property   #Prin @property transformam o metoda intr-un atribut
#     def name(self):
#         return self.__nume
#
#     @name.setter
#     def name(self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
# my_dog = Dog(nume = "Rex")
# print(my_dog.name)
#
# my_dog.name = "Ben"
# print(my_dog.name)
#
# del my_dog.name
# print(my_dog.name)


# class Cat:
#
#     legs_no  = 4
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property   #Decorator getter
#     def name(self):
#         return self.__nume
#
#     @name.setter
#     def name(self, nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
#     def change_name(self, nume):
#         self.__nume = nume
#
#     def __str__(self):
#         return f"{self.__nume}"
#
# cat_object = Cat("Fluffy")
#
# # cat_object.change_name("Milly")
# # print(cat_object)
# print(cat_object.name)
# cat_object.name = "Milly"
# print(cat_object.name)

from datetime import date

class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    @classmethod    #Nume are self ca si parametru, are cls
    def varsta_ani(cls, nume, varsta):
        return cls(nume, date.today().year - varsta)  #Inlocuieste nume cu nume si varsta cu date.today().year - varsta

    # @staticmethod    #Nume are self ca si parametru, are cls
    # def varsta_ani(varsta):
    #     return date.today().year - varsta

    @staticmethod   #O metoda independenta a clasei care poate fi accesata print denumere clasa.denumire metoda care nu tine cont de parametrii constructorului
    def stare(ani):
        return ani > 18

persoana_1 = Persoana("Ion", 21)
# print(persoana_1.varsta)
# persoana_2 = Persoana.varsta_ani("Maria", 20)
# print(persoana_2.varsta)
# print(Persoana.stare(22))
print(Persoana.varsta_ani(20))







