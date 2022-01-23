# Realizati comportamentul functiei append() utilizand functia insert().

# my_list = [5, 9, 12, 'dog', 'cat', 1492]  #define a random list
#
# def append_using_insert(list, element):
#     c = len(list)
#     list.insert(c,element)
#     print(list)
#
# append_using_insert(my_list, 88)

# Scrieti un program ce va numara cate caractere are un sir de caractere dat de utilizator. Aceasta numarare sa se realizeze cu ajutorul unui for fara a utiliza len(). La final afisati rezultatul

# sir_de_caractere=input("Please input some characters here: ")
# no_of_char = 0
# for i in sir_de_caractere:
#     no_of_char +=1
#
# print(no_of_char)

# Creati un program in care utilizatorul sa introduca o adresa de email de formatul litere_sau_cifre@litere_sau_cifre.litere.
# Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa exista o singura data in sirul de caractere

# adresa_email=input("Va rugam introduceti adresa de email: ")
# no_of_arond = 0
# no_of_dots = 0
# no_of_whitespace = 0
# validated = 1   #comutator care indica daca adresa este valida sau nu
# for i in adresa_email:  #verificam de cate ori gasim @, . sau spatii goale in adresa introdusa
#     if i=="@":
#         no_of_arond+=1
#     if i==".":
#         no_of_dots+=1
#     if i==" ":
#         no_of_whitespace+=1
#
# if no_of_arond !=1 or no_of_dots!=1 or no_of_whitespace!=0 or adresa_email.index('@')>adresa_email.index('.'):
#     print('va rugam introduceti o adresa valida de email')
#     validated = 0
#
# #Splituim adresa in partea dinainte de @ (adresa), cea dintre @ si . (domeniul1), si cea de dupa . (domeniul2)
# # Facem asta doar daca adresa pare valida dupa primele verificari
# if validated == 1:
#     list_1 = adresa_email.split("@")
#     adresa=list_1[0]
#     domeniul=list_1[1]
#     list_2=domeniul.split(".")
#     domeniul1=list_2[0]
#     domeniul2=list_2[1]
#
# #Verificam daca cele 3 stringuri obtinute sunt alfanumerice, si daca au cel putin 1 caracter fiecare
# if validated == 1:
#     if adresa.isalnum()==False or domeniul1.isalnum==False or domeniul2.isalnum()==False:
#         validated = 0
#         print('Cu exceptia @ si ., adresa trebuie sa contina doar caractere alfanumerice ')
#
#     if len(adresa)==0 or len(domeniul1)==0 or len(domeniul2)==0:
#         validated=0
#         print('Domeniul si adresa trebuie sa contina cel putin un caracter fiecare ')
# if validated==1:
#     print('Adresa dvs a fost validata. Va multumim!')

# Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
nr_de_telefon=input("Va rugam introduceti numarul de telefon (10 cifre): ")

validated = 1
if nr_de_telefon.isnumeric() == False:
    validated = 0
    print('Numarul de telefon introdus trebuie sa contina doar cifre')

if len(nr_de_telefon)!=10:
    validated= 0
    print('Numarul de telefon introdus trebuie sa contina 10 cifre')

if validated==1:
    print('Va multumim! Nr dvs de telefon a fost salvat')









# print(no_of_arond)
