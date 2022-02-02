print("Mesaj")
#format()
#a=input("Input dat de utilizator")
# def functia_mea()
    # pass

def suma(a, b, c=6):  #Se poate adauga o valoare default in functie, dar se poate suprascrie cand se schimba functia
    return a + b + c #returnarea sumei este obligatorie
#E bine de evitat utilizarea printului in functii. Va ajuta mai tarziu la clase
#Printul in functii e mai mult utilizat ca sa intelegem ce face o functia. Serverele de obicei vad printurile ca o eroare

variabila_1 = 1
variabila_2 = 2

# total = suma(variabila_1, variabila_2) #ca sa vedem parametrii care ne trebuie, apasam control + p
# print(total)

total = suma(a=variabila_1, b=variabila_2) #putem si declara care variabila e care
print(total)

#Putem da si valori default parametrilor din functii
#Atunci cand incepem sa dam valori default, sau sa definim parametri pozitionali, trebuie continuat pana la capatul parametrilor
#Incepand cu python 3.8, au fost introduse tipurile de parametri in python

def suma_b(a: int, b: int = 1, c=0) -> (int,int):  #Se poate adauga o valoare default in functie, dar se poate suprascrie cand se schimba functia
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c, a-b-c #returnarea sumei este obligatorie
#E bine de evitat utilizarea printului in functii. Va ajuta mai tarziu la clase
#Printul in functii e mai mult utilizat ca sa intelegem ce face o functia. Serverele de obicei vad printurile ca o eroare

variabila_1 = 1
variabila_2 = 2

# total = suma(variabila_1, variabila_2) #ca sa vedem parametrii care ne trebuie, apasam control + p
# print(total)

sum, dif = suma_b(a=variabila_1, c= 0, b=variabila_2) #putem declara si form
print(sum, dif)