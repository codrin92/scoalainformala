# tabla de joc
# tabla =[[' ',' ',' '],
#        [' ',' ',' '],
#        [' ',' ',' ']]
# user =input('Alege prima mutare :')
# if user == 'x'
# Declaram 3 randuri , cu cate 3 celule
# def celule
import random

choice_list = ["jucator", 'robot']
def verificare_castigator(tabla):
    if tabla[1] == tabla[2] == tabla[3] is not None or tabla[4] == tabla[5] == tabla[6] is not None or tabla[7] == tabla[8] == tabla[9] is not None or\
            tabla[1] == tabla[4] == tabla[7] is not None or tabla[8] == tabla[5] == tabla[2] is not None or tabla[9] == tabla[6] == tabla[3] is not None or\
            tabla[1] == tabla[5] == tabla[9] is not None or tabla[7] == tabla[5] == tabla[3]:
        print('Ai castigat')
def alegere_calculator(a, b):
    # Incercam 5
    if a[5] is None:
        a[5] = b
    elif a[1] is None or a[3] is None or a[7] is None or a[9] is None:
        if a[1] is None:
            a[1] = b
        elif a[3] is None:
            a[3] = b
        elif a[7] is None:
            a[7] = b
        else:
            a[9] = b
    else:
        if a[2] is None:
            a[2] = b
        elif a[4] is None:
            a[4] = b
        elif a[6] is None:
            a[6] = b
        else:
            a[8] = b
    return a


jucator = None
simbol_jucator = '0'
simbol_robot = 'x'
if random.choice(choice_list) == 'jucator':
    jucator = input('Alege valoarea:')
    simbol_robot = "0"
    simbol_jucator = "x"
tabla = {1: None, 2: None, 3: None,
         4: None, 5: None, 6: None,
         7: None, 8: None, 9: None}
print(tabla.values())
while None in list(tabla.values()):
    if jucator is None:
        jucator = input("Alege alta valoare: ")
    if tabla[int(jucator)] is None:
        tabla[int(jucator)] = simbol_jucator
    # verificare daca utilizatorul a castigat
    verificare_castigator(tabla)
    alegere_calculator(tabla, simbol_robot)
    # verificare daca calculatorul a castigat
    verificare_castigator(tabla)
    print(tabla)