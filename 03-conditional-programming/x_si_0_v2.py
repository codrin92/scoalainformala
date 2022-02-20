import random


def prnt_tic_tac_toe(board):  # 3: Functie care printeaza tabla de joc intr-un format user-friendly
    print(f" {board[0]} | {board[1]} | {board[2]} \n"
          f"___________\n"
          f" {board[3]} | {board[4]} | {board[5]} \n"
          f"___________\n"
          f" {board[6]} | {board[7]} | {board[8]} \n")


def verificare_castigator(tabla):
    if tabla[0] == tabla[1] == tabla[2] != ' ' or tabla[3] == tabla[4] == tabla[5] != ' ' \
        or tabla[6] == tabla[7] == tabla[8] != ' ' or tabla[0] == tabla[3] == tabla[6] != ' ' or\
        tabla[1] == tabla[4] == tabla[7] != ' ' or tabla[2] == tabla[5] == tabla[8] != ' ' or\
        tabla[0] == tabla[4] == tabla[8] != ' ' or tabla[2] == tabla[4] == tabla[6] != ' ':
        final_joc = 1
    elif not(tabla[0] == tabla[1] == tabla[2] != ' ' or tabla[3] == tabla[4] == tabla[5] != ' ' \
        or tabla[6] == tabla[7] == tabla[8] != ' ' or tabla[0] == tabla[3] == tabla[6] != ' ' or\
        tabla[1] == tabla[4] == tabla[7] != ' ' or tabla[2] == tabla[5] == tabla[8] != ' ' or\
        tabla[0] == tabla[4] == tabla[8] != ' ' or tabla[2] == tabla[4] == tabla[6] != ' ') and ' ' not in tabla:
        final_joc = 2  #Egalitate
    else: final_joc = 0
    return final_joc


def alegere_calculator(a, b):

    if a[4] == ' ':
        a[4] = b
    elif a[0] == ' ' or a[2] == ' ' or a[6] == ' ' or a[8] == ' ':
        if a[0] == ' ':
            a[0] = b
        elif a[2] == ' ':
            a[2] = b
        elif a[6] == ' ':
            a[6] = b
        else:
            a[8] = b
    else:
        if a[1] == ' ':
            a[1] = b
        elif a[3] == ' ':
            a[3] = b
        elif a[5] == ' ':
            a[5] = b
        else:
            a[7] = b
    return a


def x_si_0_main_function():
    choice_list = ["jucator", 'robot']
    j = 0  # :48 Initiem o variabila tip switch pentru a vedea cand e gata jocul
    jucator = None
    simbol_jucator = '0'
    simbol_robot = 'x'
    locatii_joc = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if random.choice(choice_list) == 'jucator':
        prima_mutare = 'j'
        print("Jucatorul are prima mutare.")
    else:

        prima_mutare = 'r'
        print("Calculatorul are prima mutare.")

    if prima_mutare == 'j':
        while j == 0:
            jucator = int(input('Alege locatia:'))
            while locatii_joc[jucator - 1] != ' ':
                jucator = int(input('Locatie ocupata. Alege alta locatie: '))
            locatii_joc[jucator - 1] = simbol_jucator
            prnt_tic_tac_toe(locatii_joc)
            j = verificare_castigator(locatii_joc)
            if j == 1:
                print("Jucatorul a castigat")
                return None
            if j == 2:
                print("Egalitate")
                return None
            if j == 0:
                alegere_calculator(locatii_joc, simbol_robot)
                prnt_tic_tac_toe(locatii_joc)
                j = verificare_castigator(locatii_joc)
                if j == 1:
                    print("Calculatorul a castigat")
                    return None
    else:
        while j == 0:
            alegere_calculator(locatii_joc, simbol_robot)
            prnt_tic_tac_toe(locatii_joc)
            j = verificare_castigator(locatii_joc)
            if j == 1:
                print("Calculatorul a castigat")
                return None
            if j == 2:
                print("Egalitate")
                return None
            if j == 0:
                jucator = int(input('Alege locatia:'))
                while locatii_joc[jucator - 1] != ' ':
                    jucator = int(input('Locatie ocupata. Alege alta locatie: '))
                locatii_joc[jucator - 1] = simbol_jucator
                prnt_tic_tac_toe(locatii_joc)
                j = verificare_castigator(locatii_joc)
                if j == 1:
                    print("Jucatorul a castigat")
                    return None
    return None


x_si_0_main_function()
