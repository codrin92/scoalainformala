import datetime

#Definim o functie pentru validarea codului judet. Doar anumite perechi de cifre NN din intervalul 00-99 sunt valide


def validare_cod_judet(cod_num):
    cod_judet = int(cod_num[7:9])
    l1 = [i for i in range(1, 40)]
    l2 = [j for j in range(41, 47,)]
    l3 = [51, 52]
    if cod_judet in l1 or cod_judet in l2 or cod_judet in l3:
        return 1
    else:
        print("Codul de judet este invalid. Acesta trebuie sa fie o valoare din intervalele 01-39, 41-46 sau 51-52")
        return 0


#Definim o functie care returneaza valoarea anticipata pentru cifra de control


def validare_cifra_control(cod_num):
    list_numere = [int(i) for i in cod_num]
    list_numere_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7,9]
    s_prod = sum(x * y for x, y in zip(list_numere, list_numere_control))
    rest = s_prod % 11
    if rest == 10:
        cifra_control = 1
    else:
        cifra_control = rest
    if cifra_control != int(cod_num[12]):
        print(f'CNP-ul dvs nu este valid. Cifra de control (ultima cifra) ar fi trebuit sa fie {cifra_control}')
        return 0
    else:
        return 1


def cnp_initial_checks(cnp):
    if not cnp.isnumeric():
        print('CNP-ul dvs trebuie sa contina doar cifre')
        return 0
    elif len(cnp) != 13:
        print('CNP-ul dvs trebuie sa contina 13 cifre')
        return 0
    else:
        return 1


def confirmare_secol_nastere(comutator,cnp):
    if comutator == 1:
        if cnp[0] != 0:
            anul_yy = cnp[1:3]
            if int(cnp[0]) == 1 or int(cnp[0]) == 2:
                anul_yyyy = '19' + anul_yy
                data_nasterii = anul_yyyy + cnp[3:7]
            elif int(cnp[0]) == 3 or int(cnp[0]) == 4:
                anul_yyyy = '18' + anul_yy
                data_nasterii = anul_yyyy + cnp[3:7]
            elif int(cnp[0]) == 5 or int(cnp[0]) == 6:
                anul_yyyy = '20' + anul_yy
                data_nasterii = anul_yyyy + cnp[3:7]
            else:
                anul_yyyy = '19' + anul_yy  # 27: Presupunem ca personalele cu prima cifra 7, 8, 9 sunt nascute in sec 20
                data_nasterii = anul_yyyy + cnp[3:7]
            return 1, data_nasterii
        else:
            validated = 0
            print("Prima cifra a CNP-ului dvs nu poate fi 0. Va rugam re-introduceti cnp-ul")
            data_nasterii = '000000'
            return 0, data_nasterii
    else:
        return 0, 0


def validare_data_nastere(dob):
    try:
        datetime.datetime.strptime(dob, '%Y%m%d')
        birthdatetime = datetime.datetime.strptime(dob, '%Y%m%d')
        birthdate = birthdatetime.date()
        diff = datetime.date.today() - birthdate
        if diff.days < 0:
            print('Data nasterii nu poate fi o data din viitor. Va rugam reintroduceti CNPul')
            return 0
        else:
            return 1
    except Exception:
        print("Data nasterii nu este valida. Va rugam reintroduceti CNP-ul")
        return 0


def validare_birou_ep(cod_num):
    nnn = cod_num[9:12]
    if nnn == '000':
        print("Codul pentru biroul de evidenta a populatiei nu este valid")
        return 0
    else:
        return 1


def validare_CNP_cu_functii():
    validated = 1
    cnp=input("Va rugam introduceti CNP-ul dvs. CNP-ul trebuie sa contina doar 13 cifre: ")
    validated = cnp_initial_checks(cnp)
    validated_2 = confirmare_secol_nastere(validated, cnp)
    validated = validated_2[0]
    if validated == 1:
        validated_3 = validare_data_nastere(validated_2[1])
        validated = validated_3
    if validated == 1:
        validated_4 = validare_cod_judet(cnp)
        validated = validated_4
    if validated == 1:
        validated_5 = validare_birou_ep(cnp)
        validated = validated_5
    if validated == 1:
        validated_6 = validare_cifra_control(cnp)
        validated = validated_6
    if validated == 1:
        print("Va multumin. CNP-ul dvs a fost validat cu succes")
    return None

validare_CNP_cu_functii()

