# JSON - Java Script Object Notation. Modalitate de a adauga si scrie fisiere

import json  #Asta e pachetul care trebuie importat

x = '{"name": "Ion", "age":30, "city": "Iasi"}'
y = json.loads(x)  #Asa se incarca dictionarul in JSON

print(y, type(y))

z = y
print(z, json.dumps(z), type(z)) #Asa se incarca ca si string in json

#Merge si cu liste
a = ["mere", "pere"]
print(a, json.dumps(a), type(a))

#Merge si cu string

b = "hello"
print(b, json.dumps(b), type(b))

#Merge si cu int

c = 41
print(c, json.dumps(c), type(c))

#Merge si cu boolean

d = False
print(d, json.dumps(d), type(d))

#Merge si cu None

e = None
print(e, json.dumps(e), type(e))