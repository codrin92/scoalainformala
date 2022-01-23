#Tema 1
# Creați un script Python care îndeplinește următoarele funcții:
# ○ declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
# ○ afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# ○ afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
# ○ afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
# ○ afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
# ○ afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).

my_list = [7,8,9,2,3,1,4,10,5,6]
my_list_copy = my_list  #creare copie pentru operatiuni - pastram lista originala

my_list_copy.sort()    #sortare ascendenta
print(my_list_copy)    #printare sortare ascendenta

my_list_copy.sort(reverse=True)    #sortare descendenta
print(my_list_copy)    #printare sortare descendenta

my_list_copy.sort() #revenim la lista ordonata initial

my_sliced_list = my_list_copy[1::2] #slice pt numere pare - merge doar pt ca lucram deja cu o lista ordonata si consecutiva
print(my_sliced_list)

my_sliced_list = my_list_copy[0::2] #slice pt numere impare - merge doar pt ca lucram deja cu o lista ordonata si consecutiva
print(my_sliced_list)

my_sliced_list = my_list_copy[2::3] #slice pt numere multipli de 3 - merge doar pt ca lucram deja cu o lista ordonata si consecutiva
print(my_sliced_list)