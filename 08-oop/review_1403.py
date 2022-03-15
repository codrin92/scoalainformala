class ClasaMea:
    gamma = 0  #Atribut sau variabila de clasa

    def __init__(self):  #Constructorul initializeaza valorile dintr-un obiect
        self.alpha = 1  # variabila de instanta sau proprietate (pentru ca este definita in constructa)
        self.__delta = 3  #Variabila de instanta privata

obj = ClasaMea()   #Instantiere a clasei ClasaMea. Asa definim un obiect
obj.beta = 2   #Variabila de instanta care exista doar in interiorul obiectului 'obj'
print(obj.__dict__)  #Dictionar de parametri ai clasei
print(obj.alpha)
print(ClasaMea.gamma)
print(obj._ClasaMea__delta)  #Felul in care afiseaza dictul indica si felul in care putem accesa variabile, mai ales cele private
