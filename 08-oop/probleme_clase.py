# class Catalog:
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f" \t Nume : {self.nume} \n \t Prenume : {self.prenume} \n \t Absente : {self.absente} \n \t Materii si note {self.materii}"
#
#     def incrementAbs(self):
#         self.absente += 1
#
#     def subtractAbs(self, scutite):
#         if self.absente >= scutite:
#             self.absente -= scutite
#
#
# class Extensie1(Catalog):
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#
#     def add_subject(self, materie, note):
#         self.materii.update({materie:note})
#
#     def print_all_subjects(self):
#         return f"{self.materii.keys()}"
#
#     def average_grades(self):
#
#         note_finale = {}
#         for i,j in self.materii.items():
#             if all(isinstance(x, int) for x in j):
#                 media = sum(j)/len(j)
#                 note_finale.update({i : media})
#         return note_finale





# student = Catalog("Roata", "Ion")
# print(student)
# student.incrementAbs()
# student.incrementAbs()
# student.incrementAbs()
# print(student)
#
# student.subtractAbs(2)
# print(student)

# gigi = Extensie1("Ana", "Mere")
# gigi.add_subject("Gee i'm a tree", [4, 6, 7])
# gigi.add_subject("history", [1,2])
#
# gigi.average_grades()
#
# print(gigi.average_grades())

from operator import itemgetter

class Catalog_Prajituri:
    lista_prajituri = []
    def __init__(self, nume = "Chec", pret = 100, gramaj = 400):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        caracteristici_obiect = [self.nume, self.pret, self.gramaj]
        self.lista_prajituri.append(caracteristici_obiect)

    @staticmethod
    def sortare_pret():
        sortata_pret = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(1))
        return f"Prajiturile sortate dupa pret sunt {sortata_pret}"

    @staticmethod
    def sortare_gramaj():
        sortata_gramaj = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(2))
        return f"Prajiturile sortate dupa gramaj sunt {sortata_gramaj}"

class Tort(Catalog_Prajituri):
    def __init__(self, nume, gramaj, pret, etajat = False, glazura = "ciocolata"):
        super().__init__(nume, gramaj, pret)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f"Etajarea este {self.etajat} iar glazura este {self.glazura}"

class Fursec(Catalog_Prajituri):
    pass
    # def __init__(self):
    #     super().__init__()

prj1=Catalog_Prajituri("Eclere", 10, 300)
prj2=Catalog_Prajituri("Ecler mic", 7, 115)
prj3=Catalog_Prajituri("Lava", 15, 275)

tort1 = Tort(nume = "A", gramaj = 112, pret = 150, etajat = True, glazura = "cacao")
tort2 = Tort(nume = "D", gramaj = 55, pret = 45, etajat = True, glazura = "cacao")
tort3 = Tort(nume = "B", gramaj = 1150, pret = 350, etajat = True, glazura = "cacao")

fursec1 = Fursec()
# print(fursec1.nume)

print(Catalog_Prajituri.lista_prajituri)

print(Catalog_Prajituri.sortare_gramaj())

# print(Catalog_Prajituri.sortare_pret())


# print(tort1.glazura)
# print(tort1.gramaj)
# print(tort1.nume)
#
# print(tort1)





