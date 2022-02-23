import pandas as pd  #Se foloseste aliasul pd

#Pandas este o librarie pe care o putem folosi pt citire si parsare de date, si pt statistica in python

# # Se poate lucra cu dictionare
# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
#
# variabila = pd.DataFrame(dictionar_date)
# print(variabila)
#
# #Se poate lucra cu serii
#
# masini = ['Dacia', 'Volvo', 'Renault']
# variabila = pd.Series(masini)
# print(variabila[0])
#
# #Putem adauga noi indexii nostri preferati
#
# # masini = ['Dacia', 'Volvo', 'Renault']
# # variabila = pd.Series(masini, index=["x","y","z"])
# # print(variabila)
# # print(variabila["z"])
# # print(variabila[0])  #Se poate accesa valoarea si prin intermediul indexului default
#
# masini = {"x":"Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini)
# print(variabila)
#
# masini = {"x":"Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini, index=["y", "z"])
# print(variabila)

# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": ['rosu', 'alb', 'verde']
# }
#
# # variabila = pd.DataFrame(dictionar_date)
# # print(variabila)
# # print(variabila.loc[0])  #Se afiseaza randul cu indexul 0
# # print(variabila.loc[[0, 1]])  #Se afiseaza randurile cu indexurile 0 si 1
#
# variabila = pd.DataFrame(dictionar_date, index = ["producator1", "producator2", "producator3"])
# print(variabila)  #Se afiseaza randurile cu indexurile 0 si 1
# # print(variabila.loc["producator1"])  #Se afiseaza randurile cu indexurile 0 si 1
# # print(variabila.loc[0]) #Indexul default nu merge atunci cand lucram cu dictionare
# print(variabila.loc[["producator1", "producator2"]])
#

# data = {
#   "producator1": {
#     "masini": "Dacia",
#     "culoare": "rosu"
#   },
#   "producator2": {
#     "masini": "Volvo",
#     "culoare": "alb"
#   },
#   "producator3": {
#     "masini": "Renault",
#     "culoare": "verde"
#   }
# }
#
#
# variabila1 = pd.DataFrame(data)
# variabila1 = pd.read_json('data.json')

#Ca sa citim un json de pe un site

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url='https://api.exchangerate-api.com/v4/latest/USD'
# variabila1 = pd.read_json(url)
# print(variabila1)

data = {
  "producator1": {
    "masini": "Dacia",
    "culoare": "rosu"
  },
  "producator2": {
    "masini": "Volvo",
    "culoare": "alb"
  },
  "producator3": {
    "masini": "Renault",
    "culoare": "verde"
  }
}


#Ca sa salvam datele intr-un CSV

variabila1 = pd.DataFrame(data)
fisier = variabila1.to_csv("data.csv")

