import datetime
import csv
import pandas as pd

# Definim o variabila in care se stocheaza categoriile

lista_categorii = []

print("Bine ati venit. Va rugam introduceti categoriile de task-uri dorite")

#Introducem toate categoriile dorite
introducere_categorii = "y"

while introducere_categorii == "y":
    categorie = input("Va rog introduceti categoria dorita: ").lower()
    if categorie in lista_categorii:
        print("Categoria introdusa este deja stocata. Va rog introduceti alta categorie")
    else:
        lista_categorii.append(categorie)
    decizie = input("Doriti sa introduceti si alta categorie? (y/n)").lower()
    while decizie not in "yn":
        decizie = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    introducere_categorii = decizie

print("Multumim ca ati introdus categoriile. Va rugam introduceti taskurile")

#Introducem toate taskurile dorite

introducere_taskuri = "y"
index_taskuri = 0
lista_taskuri = []
lista_de_liste_taskuri=[]

while introducere_taskuri == "y":
    nume_task = input("Va rog introduceti numele taskului: ").lower()
    if nume_task in lista_taskuri:
        print("Taskul a fost deja introdus. Va rog introduceti alt task")
    else:
        lista_taskuri.append(nume_task)
        task = ["","","",""]
        task[0] = nume_task
        data_buna = False
        while not data_buna:
            data_si_ora = input("Va rugam specificati data limita pentru introducerea taskului. Formatul trebuie sa fie zz.ll.aaaa hh:mm:")
            try:
                datetime.datetime.strptime(data_si_ora, '%d.%m.%Y %H:%M')
                data_corecta_task = datetime.datetime.strptime(data_si_ora, '%d.%m.%Y %H:%M')
                task[1] = data_corecta_task
                data_buna = True
            except Exception:
                print("Data introdusa nu are un format valid. Va rugam introduceti un format valid")
        persoana_responsabila_task = input("Va rugam introduceti persoana responsabila pentru task:").lower()
        task[2] = persoana_responsabila_task
        categorie_buna = False
        while not categorie_buna:
            categorie_task = input(f"Va rugam introduceti categoria taskului. Aceasta trebuie sa fie una din lista {lista_categorii}:").lower()
            if categorie_task in lista_categorii:
                task[3] = categorie_task
                categorie_buna = True
            else:
                print("Categoria introdusa nu se afla in lista de categorii. Va rugam reincercati")
        lista_de_liste_taskuri.append(task)
    decizie_task = input("Doriti sa introduceti si alt task? (y/n)").lower()
    while decizie_task not in "yn":
        decizie_task = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    introducere_taskuri = decizie_task

with open('data_categorii.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(lista_categorii)

with open('data_taskuri.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for task in lista_de_liste_taskuri:
        csv_writer.writerow(task)

#
# print(lista_categorii)
# print(lista_de_liste_taskuri)
#
optiune_valida = False
while not optiune_valida:
    optiune = input("Va rugam alegeti o optiune: 1. Listare date 2. Sortare date 3. Filtrare date 4. Adaugare task "
                    "5. Editare task 6. Stergere task: ")
    if optiune.isdigit() == True and int(optiune) in [1, 2, 3, 4, 5, 6]:
        optiune_valida = True
    else:
        print("Va rugam alegeti o optiune valida (1-6). 1. Listare date 2. Sortare date 3. Filtrare date "
              "4. Adaugare task 5. Editare task 6. Stergere task: ")

if int(optiune) == 1:
    data = pd.read_csv('data_taskuri.csv', header=None)
    data.sort_values(data.columns[3], axis=0, ascending=True, inplace=True)
    print(data)

elif int(optiune) == 2:   #Userul a ales sa primeasca informatii sortate ca si output
    optiune_valida_sortare = False
    while not optiune_valida_sortare:
        optiune_sortare = input("Va rugam alegeti o optiune: 1. Task ascendent 2. Task descendent 3. Data ascendent "
                                "4. Data descendent 5. Persoana ascendent 6. Persoana descendent"
                                "7. Categorie ascendent 8. Categorie descendent:")
        if optiune_sortare.isdigit() == True and int(optiune_sortare) in [1, 2, 3, 4, 5, 6, 7, 8]:
            optiune_valida_sortare = True
        else:
            print("Va rugam alegeti o optiune valida: 1. Task ascendent 2. Task descendent 3. Data ascendent "
                  "4. Data descendent 5. Persoana ascendent 6. Persoana descendent 7. Categorie ascendent "
                  "8. Categorie descendent:")
    if int(optiune_sortare) == 1:  #Sortare ascendenta dupa task
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[0], axis=0, ascending=True, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_1.csv")   #Folosim index diferit la output file pt a intelege optiunile alese
    elif int(optiune_sortare) == 2:  #Sortare descendenta dupa task
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[0], axis=0, ascending=False, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_2.csv")
    elif int(optiune_sortare) == 3:  #Sortare ascendenta dupa data
        data = pd.read_csv('data_taskuri.csv', header=None)
        data[1] = pd.to_datetime(data[1])
        data.sort_values(data.columns[1], axis=0, ascending=True, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_3.csv")
    elif int(optiune_sortare) == 4:  # Sortare descendenta dupa data
        data = pd.read_csv('data_taskuri.csv', header=None)
        data[1] = pd.to_datetime(data[1])
        data.sort_values(data.columns[1], axis=0, ascending=False, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_4.csv")
    elif int(optiune_sortare) == 5:  # Sortare ascendenta dupa persoana responsabila
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[2], axis=0, ascending=True, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_5.csv")
    elif int(optiune_sortare) == 6:  # Sortare descendenta dupa persoana responsabila
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[2], axis=0, ascending=False, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_6.csv")
    elif int(optiune_sortare) == 7:  # Sortare ascendenta dupa categorie
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[3], axis=0, ascending=True, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv(f"sorted_output_2_7.csv")
    else:  #Sortare descendenta dupa categorie
        data = pd.read_csv('data_taskuri.csv', header=None)
        data.sort_values(data.columns[3], axis=0, ascending=False, inplace=True)
        data_sorted = pd.DataFrame(data)
        fisier = data_sorted.to_csv("sorted_output_2_8.csv")

elif int(optiune) == 3: #Userul a ales sa primeasca informatii filtrate ca si output
    optiune_valida_filtrare = False
    while not optiune_valida_filtrare:
        optiune_filtrare = input("Va rugam alegeti o caracteristica dupa care sa se efectueze filtrarea datelor:/"
                                 ": 1. Nume task 2. Data task 3. Persoana responsabila task 4. Categorie task")
        if optiune_filtrare.isdigit() == True and int(optiune_filtrare) in [1, 2, 3, 4]:
            optiune_valida_filtrare = True
        else:
            print("Va rugam alegeti o caracteristica valida dupa care sa se efectueze filtrarea datelor:/"
                  ": 1. Nume task 2. Data task 3. Persoana responsabila task 4. Categorie task")
    text_filtrare = input("Va rugam introduceti caracterele folosite pentru filtrare:")
    if int(optiune_filtrare) == 1: #Filtrare dupa nume task
        data = pd.read_csv('data_taskuri.csv', header=None)
        filtered_frame = data[data[0].str.contains(text_filtrare)]
        data_filtered = pd.DataFrame(filtered_frame)
        fisier = data_filtered.to_csv("sorted_output_3_1.csv")
    elif int(optiune_filtrare) == 2: #Filtrare dupa data task
        data = pd.read_csv('data_taskuri.csv', header=None)
        filtered_frame = data[data[1].str.contains(text_filtrare)]
        data_filtered = pd.DataFrame(filtered_frame)
        fisier = data_filtered.to_csv("sorted_output_3_2.csv")
    elif int(optiune_filtrare) == 3: #Filtrare dupa nume persoana responsabila
        data = pd.read_csv('data_taskuri.csv', header=None)
        filtered_frame = data[data[2].str.contains(text_filtrare)]
        data_filtered = pd.DataFrame(filtered_frame)
        fisier = data_filtered.to_csv("sorted_output_3_3.csv")
    else:                            #Filtrare dupa categorie task
        data = pd.read_csv('data_taskuri.csv', header=None)
        filtered_frame = data[data[3].str.contains(text_filtrare)]
        data_filtered = pd.DataFrame(filtered_frame)
        fisier = data_filtered.to_csv("sorted_output_3_4.csv")

elif int(optiune) == 4:  #Userul a ales sa adauge un task
    task_nou = False
    task_2 =['','','','']
    while not task_nou:
        n_task = input("Va rugam introduceti numele taskului care trebuie adaugat: ")
        data = pd.read_csv('data_taskuri.csv', header=None)
        print(data[0])
        if n_task in data[0].values:
            print("Taskul este deja prezent in lista de taskuri")
        else:
            task_nou = True
    task_2[0] = n_task
    data_buna_2 = False
    while not data_buna_2:
        data_si_ora_2 = input("Va rugam specificati data limita pentru introducerea taskului. Formatul trebuie sa fie zz.ll.aaaa hh:mm:")
        try:
            datetime.datetime.strptime(data_si_ora_2, '%d.%m.%Y %H:%M')
            data_corecta_task_2 = datetime.datetime.strptime(data_si_ora_2, '%d.%m.%Y %H:%M')
            task_2[1] = data_corecta_task_2
            data_buna_2 = True
        except Exception:
            print("Data introdusa nu are un format valid. Va rugam introduceti un format valid")
    persoana_responsabila_task_2 = input("Va rugam introduceti persoana responsabila pentru task:").lower()
    task_2[2] = persoana_responsabila_task_2
    categorie_buna_2 = False
    while not categorie_buna_2:
        categorie_task_2 = input(f"Va rugam introduceti categoria taskului. Aceasta trebuie sa fie una din lista {lista_categorii}:").lower()
        if categorie_task_2 in lista_categorii:
            task_2[3] = categorie_task_2
            categorie_buna_2 = True
        else:
            print("Categoria introdusa nu se afla in lista de categorii. Va rugam reincercati")

    with open('data_taskuri.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(task_2)

elif int(optiune) == 5:  #Userul a ales sa modifice un task
    data = pd.read_csv('data_taskuri.csv', header=None)
    print(data)
    no_of_tasks = data.shape[0]
    task_selected = False
    while not task_selected:
        task_to_change = input(f"Va rugam alegeti taskul care trebuie schimbat. Acesta are un index de la 0 la {no_of_tasks-1}:")
        if task_to_change.isnumeric() and int(task_to_change) >= 0 and int(task_to_change) <= no_of_tasks-1:
            task_selected = True
        else:
            print("Alegeti alt task")
    schimbare_data = False
    opt_schimbare_nume = input("Doriti sa schimbati numele taskului (y/n)?").lower()   #Schimbare nume de task   -Nu am facut inca validare pe nume
    while opt_schimbare_nume not in "yn":
        opt_schimbare_nume = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    if opt_schimbare_nume == "y":
        nume_nou_pt_task = input("Introduceti numele nou pt taskul dvs:").lower()
        data.iat[int(task_to_change), 0] = nume_nou_pt_task
    opt_schimbare_data = input("Doriti sa schimbati data taskului (y/n)?").lower()      #Schimbare data de task  - Nu am facut inca validare pe data
    while opt_schimbare_data not in "yn":
        opt_schimbare_data = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    if opt_schimbare_data == "y":
        data_noua_pt_task = input("Introduceti data noua pt taskul dvs:")
        data.iat[int(task_to_change), 1] = data_noua_pt_task
    opt_schimbare_pers = input("Doriti sa schimbati persoana responsabila pt task (y/n)?").lower()      #Schimbare persoana task
    while opt_schimbare_pers not in "yn":
        opt_schimbare_pers = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    if opt_schimbare_pers == "y":
        pers_noua_pt_task = input("Introduceti persoana noua pt taskul dvs:").lower()
        data.iat[int(task_to_change), 2] = pers_noua_pt_task
    opt_schimbare_categorie = input("Doriti sa schimbati categoria taskului (y/n)?").lower()            #Schimbare categorie task  - nu am facut inca validare pe categorii
    while opt_schimbare_categorie not in "yn":
        opt_schimbare_categorie = input("Va rugam introduceti o decizie valida (y/n): ").lower()
    if opt_schimbare_categorie == "y":
        categorie_noua_pt_task = input("Introduceti categoria noua pt taskul dvs:").lower()
        data.iat[int(task_to_change), 3] = categorie_noua_pt_task

    fisier = data.to_csv("modified_output_5.csv")

else:   #Userul a ales sa stearga un task - E singura optiune ramasa
    data = pd.read_csv('data_taskuri.csv', header=None)
    no_of_tasks = data.shape[0]
    print(data)
    task_selected = False
    while not task_selected:
        task_to_change = input(
            f"Va rugam alegeti taskul care trebuie sters. Acesta are un index de la 0 la {no_of_tasks - 1}:")
        if task_to_change.isnumeric() and int(task_to_change) >= 0 and int(task_to_change) <= no_of_tasks - 1:
            task_selected = True
        else:
            print("Alegeti alt task")
    data.drop(int(task_to_change), axis=0, inplace=True)
    fisier = data.to_csv("modified_output_6.csv")

# print(data)
# print(data.iat[int(task_to_change), 0])


# print(data)
# print(data.shape)
# print(data.shape[0])

#Filtrare dupa nume de task



# print(data_filtered)

# with open('sorted_output_1.csv', 'a', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for rand in data:
#         csv_writer.writerow(rand)





