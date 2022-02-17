#Pentru deschiderea unui fisier, folosim with

# with open("fisier.txt", "w") as file:  #dupa numele fisierului, se defineste modul de deschiere read only r care e si default/write w /append a - da
# # /r datele se pierd/ r+ drepture de scriere si citire
#     file.write("Buna seara")

#Metoda alternativa de deschidere

# file = open("fisier.txt", "w")
# file.write("Buna")
# # file.close

# file = open("fisier.txt", "w")
# try:
#     file.write("Buna ziua")
# except Exception:
#     pass
# finally:
#     file.close()

# with open("fisier1.txt", "w") as file:
#     file.write("Buna seara")  #Cand rulam, daca fisierul nu exista, este creat automat


# with open("fisier2.txt", "a") as file:
#     file.write("Buna dimineata1")

# with open("fisier2.txt", "r") as file:
#     for line in file.readlines():
#         print("line", line)

with open("fisier2.txt", "r") as file:
    for line in list(file):
        print("line", line)

