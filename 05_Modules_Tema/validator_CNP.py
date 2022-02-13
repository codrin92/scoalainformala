import datetime

#Definim o functie pentru validarea codului judet. Doar anumite perechi de cifre NN din intervalul 00-99 sunt valide
def validare_cod_judet(cod_num):
    cod_judet = int(cod_num[7:9])
    l1 = [i for i in range(1, 40)]
    l2 = [j for j in range(41, 47,)]
    l3 = [51, 52]
    if cod_judet in l1 or cod_judet in l2 or cod_judet in l3:
        jj = 1
    else:
        jj = 0
    return jj

#Definim o functie care returneaza valoarea anticipata pentru cifra de control
def validare_sum_product(cod_num):
    list_numere = [int(i) for i in cod_num]
    list_numere_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7,9]
    s_prod = sum(x * y for x, y in zip(list_numere, list_numere_control))
    rest = s_prod % 11
    if rest == 10:
        cifra_control = 1
    else:
        cifra_control = rest
    return cifra_control

cnp=input("Va rugam introduceti CNP-ul dvs. CNP-ul trebuie sa contina doar 13 cifre: ")

#Definim un parametru switch care permite rularea blocurilor de instructiuni pe masura ce CNPul este testat
validated = 1

#Verificam daca datele introduse sunt numerice

if cnp.isnumeric() == False:
    validated = 0
    print('CNP-ul dvs trebuie sa contina doar cifre')

#Verificam numarul de cifre din CNP
if len(cnp)!=13:
    validated= 0
    print('CNP-ul dvs trebuie sa contina 13 cifre')

#Confirmam secolul nasterii, in functie prima cifra, pentru stabilirea anului exact
if validated == 1:
    if cnp[0] != 0:
        anul_yy = cnp[1:3]
        if int(cnp[0]) == 1 or int(cnp[0]) == 2:
            anul_yyyy = '19' + anul_yy
        elif int(cnp[0]) == 3 or int(cnp[0]) == 4:
            anul_yyyy = '18' + anul_yy
        elif int(cnp[0]) == 5 or int(cnp[0]) == 6:
            anul_yyyy = '20' + anul_yy
        else:
            anul_yyyy = '19' + anul_yy # 27: Presupunem ca personalele cu prima cifra 7, 8, 9 sunt nascute in sec 20
    else:
        validated == 0
        print("Prima cifra a CNP-ului dvs nu poate fi 0. Va rugam re-introduceti cnp-ul")
        anul_yyyy = 0
    if anul_yyyy != 0:
        data_nasterii = anul_yyyy+cnp[3:7]
    else:
        validated = 0
        data_nasterii = '000000'

#Verificam validitatea datei de nastere. Testul 1: Verificam daca data este o data valida din calendar
if validated == 1:
    try:
        datetime.datetime.strptime(data_nasterii, '%Y%m%d')
    except Exception:
        print("Data nasterii nu este valida. Va rugam reintroduceti CNP-ul")
        validated = 0

#Verificam validitatea datei de nastere. Testul 2: Verificam daca data este una din trecut
if validated == 1:
    birthdatetime = datetime.datetime.strptime(data_nasterii, '%Y%m%d')
    birthdate = birthdatetime.date()
    diff = datetime.date.today() - birthdate
    if diff.days < 0:
        validated = 0
        print('Data nasterii nu poate fi o data din viitor. Va rugam reintroduceti CNPul')

#Verificam validitatea codului de judet
if validated == 1:
    validated = validare_cod_judet(cnp)
    if validated == 0:
        print("Codul de judet este invalid. Acesta trebuie sa fie o valoare din intervalele 01-39, 41-46 sau 51-52")

#Verificam validitatea codului pentru biroul de evidenta a populatiei
if validated == 1:
    nnn = cnp[9:12]
    if nnn == '000':
        print("Codul pentru biroul de evidenta a populatiei nu este valid")

#Verificam cifra de control

if validated == 1:
    cifra_13_expected = validare_sum_product(cnp)  #Calculam cat ar trebui sa fie ultima cifra, in baza formulei
    cifra_13 = int(cnp[12])
    if cifra_13_expected != cifra_13:
        validated == 0
        print(f'CNP-ul dvs nu este valid. Cifra de control (ultima cifra) ar fi trebuit sa fie {cifra_13_expected}')

if validated == 1:
    print("Va multumim. CNP-ul dvs a fost validat cu succes")
