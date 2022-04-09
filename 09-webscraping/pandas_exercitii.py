import pandas as pd
import matplotlib.pyplot as plt

#print(pd.__version__)

# a = {'x': 1, "y": 7, "z": 2}
# variabila = pd.Series(a, index=a.keys())
# variabila_2=pd.Series(a, index = ['x', 'y'])
#
# print(variabila)
# print(variabila_2)

# data = {
#     "key1": [0, 1, 2],
#     "key2": [3, 4, 5]
# }
#
# # variabila_3 = pd.DataFrame(data)
# variabila_3 = pd.DataFrame(data, index = ['linie1', 'linie2', 'linie3'])
# print(variabila_3)
# print(variabila_3['key2'])  #Printeaza doar valorile de pe o cheie. Key 2, coloana
# print(variabila_3.loc['linie2']) #Printeaza doar valorile de pe un rand

# df=pd.read_csv('Exemplu.csv')
# print(df)
#
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
# df = pd.DataFrame(data)
# print(df)
#
df = pd.read_csv('test.csv')
# # print(df)
# df1 = None
# for x in df.index:
#   if df.loc[x, 'AL'] == ': ':
#     df1 = df.drop(x, inplace=False)
# #
# print(df)
# print(df1)
# df1 = df.to_csv('test1.csv')
# print(df.corr())   #Corelatii
# print(df.describe()) #Descrierea data frameului
# print(df.mean())
# df.plot(kind = 'scatter', x = 'AT', y= 'BE')  #Plotare graph
# df['AT'].plot(kind='hist')                     #Plotare histograma
# plt.show()

# print(df.head(2))   #Afiseaza primele 2 randuri
# print(df.tail(3))   #Afiseaza ultimee 3 randuri
new_df = df.dropna(inplace=False)
print(df)
print(new_df)
df['AL'].fillna(0,inplace=True)   #Se inlocuiesc valorile NA cu valorile cerute
print(df)

df.loc[7, 'AL'] = 45  #Se inlocuieste o valoare anume cu valoarea dorita
print(df)

df.replace(': ', 0, inplace=True)
print(df)
print(df.transpose())
df.to_csv('test1.csv')
