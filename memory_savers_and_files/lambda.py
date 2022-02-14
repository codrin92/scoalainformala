# my_lambda = lambda x, y: x + y
# #denumire functie = labda param1, param2: corp functie
# my_sum = my_lambda(2, 3)
# print(my_sum)

# PEP8 recomdanda utilizarea def

diferenta = lambda x, y: x - y

my_diff = diferenta(4, 2)
print(my_diff)

players =[{"first_name": "Ion", "last_name": "Gheorghe", "varsta": 12},
          {"first_name": "Andreea", "last_name": "Popa", "varsta": 35},
          {"first_name": "Isabela", "last_name": "Enache", "varsta": 25}]

jucatori_sortati = sorted(players, key= lambda jucator: jucator["varsta"])  #Functia sorted itereaza prin fiecare dictionar si gaseste varsta
print(jucatori_sortati)

jucatori_sortati = sorted(players, key= lambda jucator: jucator["first_name"])  #Functia sorted itereaza prin fiecare dictionar si gaseste varsta
print(jucatori_sortati)