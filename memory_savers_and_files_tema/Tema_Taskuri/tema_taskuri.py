import datetime
import csv
import pandas as pd

#Definim o variabila in care se stocheaza categoriile
#
# lista_categorii = []
#
# print("Bine ati venit. Va rugam introduceti categoriile de task-uri dorite")
#
# #Introducem toate categoriile dorite
# introducere_categorii = "y"
#
# while introducere_categorii == "y":
#     categorie = input("Va rog introduceti categoria dorita: ").lower()
#     if categorie in lista_categorii:
#         print("Categoria introdusa este deja stocata. Va rog introduceti alta categorie")
#     else:
#         lista_categorii.append(categorie)
#     decizie = input("Doriti sa introduceti si alta categorie? (y/n)").lower()
#     while decizie not in "yn":
#         decizie = input("Va rugam introduceti o decizie valida (y/n): ").lower()
#     introducere_categorii = decizie
#
# print("Multumim ca ati introdus categoriile. Va rugam introduceti taskurile")
#
# #Introducem toate taskurile dorite
#
# introducere_taskuri = "y"
# index_taskuri = 0
# lista_taskuri = []
# lista_de_liste_taskuri=[]
#
# while introducere_taskuri == "y":
#     nume_task = input("Va rog introduceti numele taskului: ").lower()
#     if nume_task in lista_taskuri:
#         print("Taskul a fost deja introdus. Va rog introduceti alt task")
#     else:
#         lista_taskuri.append(nume_task)
#         task = ["","","",""]
#         task[0] = nume_task
#         data_buna = False
#         while not data_buna:
#             data_si_ora = input("Va rugam specificati data limita pentru introducerea taskului. Formatul trebuie sa fie zz.ll.aaaa hh:mm:")
#             try:
#                 datetime.datetime.strptime(data_si_ora, '%d.%m.%Y %H:%M')
#                 data_corecta_task = datetime.datetime.strptime(data_si_ora, '%d.%m.%Y %H:%M')
#                 task[1] = data_corecta_task
#                 data_buna = True
#             except Exception:
#                 print("Data introdusa nu are un format valid. Va rugam introduceti un format valid")
#         persoana_responsabila_task = input("Va rugam introduceti persoana responsabila pentru task:").lower()
#         task[2] = persoana_responsabila_task
#         categorie_buna = False
#         while not categorie_buna:
#             categorie_task = input(f"Va rugam introduceti categoria taskului. Aceasta trebuie sa fie una din lista {lista_categorii}:").lower()
#             if categorie_task in lista_categorii:
#                 task[3] = categorie_task
#                 categorie_buna = True
#             else:
#                 print("Categoria introdusa nu se afla in lista de categorii. Va rugam reincercati")
#         lista_de_liste_taskuri.append(task)
#     decizie_task = input("Doriti sa introduceti si alt task? (y/n)").lower()
#     while decizie_task not in "yn":
#         decizie_task = input("Va rugam introduceti o decizie valida (y/n): ").lower()
#     introducere_taskuri = decizie_task
#
# with open('data_categorii.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     csv_writer.writerow(lista_categorii)
#
# with open('data_taskuri.csv', 'a', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for task in lista_de_liste_taskuri:
#         csv_writer.writerow(task)


# print(lista_categorii)
# print(lista_de_liste_taskuri)

#Listare date

# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[3], axis=0, ascending=True, inplace=True)
#
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_1.csv")

#Sortare date
#1. sortare ascendentă task
# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[0], axis=0, ascending=True, inplace=True)
#
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_1.csv")


#2. sortare descendentă task

# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[0], axis=0, ascending=False, inplace=True)
#
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_2.csv")

#3. sortare ascendentă data
# data = pd.read_csv('data_taskuri.csv', header=None)
# data[1] = pd.to_datetime(data[1])
# data.sort_values(data.columns[1], axis=0, ascending=True, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_3.csv")

#
#4. sortare descendentă data

# data = pd.read_csv('data_taskuri.csv', header=None)
# data[1] = pd.to_datetime(data[1])
# data.sort_values(data.columns[1], axis=0, ascending=False, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_4.csv")
#
# #
# #5. sortare ascendentă persoana responsabilă
#
# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[2], axis=0, ascending=True, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_5.csv")
# #
# #6. sortare descendentă persoană responsabilă
#
# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[2], axis=0, ascending=False, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_6.csv")
# #
# #7. sortare ascendentă categorie
#
# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[3], axis=0, ascending=True, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_7.csv")
#
# #8. sortare descendentă categorie
#
# data = pd.read_csv('data_taskuri.csv', header=None)
# data.sort_values(data.columns[3], axis=0, ascending=False, inplace=True)
# data_sorted = pd.DataFrame(data)
# fisier = data_sorted.to_csv("sorted_output_2_8.csv")



#Filtrare dupa nume de task

data = pd.read_csv('data_taskuri.csv', header=None)
filtered_frame = data[data[0].str.contains('ma')]
data_filtered = pd.DataFrame(filtered_frame)
fisier = data_filtered.to_csv("sorted_output_3_1.csv")

print(data_filtered)

# with open('sorted_output_1.csv', 'a', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for rand in data:
#         csv_writer.writerow(rand)





