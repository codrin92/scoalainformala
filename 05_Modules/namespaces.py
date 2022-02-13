#Un namespace este ca un dictionare unde cheia este numele obiectului, iar valoarea este valoarea obiectului

#Sunt create doar cand executam, sunt sterse atunci cand nu mai sunt necesare
#Pot exista mai multe namespaces intr-un program

#Cu dir(__builtins__) gasim obiectele standard

# def my_function():
#     msg="Hello"
#     print(msg)
#     return None
#
# my_function()
# print(msg) #Daca rulam, ni se va zice ca msg nu este definit. Asta de din cauza ca msg este definit doar in namespaceul functiei
#
# #Pentru definirea globala, se foloseste comanda 'global'
# def my_function():
#     global msg
#     msg="Hello"
#     print(msg)
#     return None
#
# my_function()
# print(msg)

# def my_function(): #enclosing function
#     def my_second_function(): #enclosed function
#         print(f"functia mea secundara: {msg}")
#         return None
#     msg="Hello"
#
#     my_second_function()
#     print(f"functia mea principala: {msg}")
#
#     return None
#
# my_function()


# def my_function():  # enclosing function
#     def my_second_function():  # enclosed function
#         global msg
#         msg = "Hello"
#         print(f"functia mea secundara: {msg}")
#         return None
#
#     my_second_function()
#     print(f"functia mea principala: {msg}")
#     return None
#
#
# my_function()
# print(msg)


