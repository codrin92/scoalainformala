#1
#My choice b. 16
#Ok

# num_calls = 0
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
# print(exercitiu(4))

#2
#My choice c. 1 1
#Ok
# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())

#3
#My choice is b. 5
#Ok

#4
#My choice is d. Type error
#Ok
# x=(1, 2, 3)
# x[1] = 4

#5
#My choice is d. 1, 2, 3, 4, 5, 4, 5, 4, 5
#Ok

# a = [1, 2, 3]
# b = [4, 5]
# print(a+b*3)

#6
# My choice is b. 4
#Ok
# x = [1, 2, 3, 4]
# print(x[-1:])

#7
# My choice is [0, 1, 2]
#Ok
# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

#8
#My choice is 0, 1, 2
#Gresit. La return se va iesi la 0

# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)

#9
#My choice is c [0, 4, 16, 36, 64
#ok
# a=range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)

#10
#My choice is c. 10
#Ok
# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a, 10))

#11
#My choice is d. 100
#Ok

# class BankAccount():
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
# a = BankAccount()
# b = BankAccount()
# print(a.deposit(100))

#12
#My choice is a. cannot concatenate str and int
#Ok

# "foo" + 2

#13
#My choice is a, c, d
#Ok
# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

#14
#My choice is x, y
#Ok
# for k in {"x": 1, "y":2}:
#     print(k)

#15
#My choice is ['p', 'y', 't', 'h', 'o', 'n']
#Ok
#
# print(list("python"))

#16
#My choiuce is 6
#Ok
#
# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))

#17
#My choice is loop infinit
#Ok
# count = (3, 2, 5, 4)
# while len(count)<5:
#     count0=count[0]+1
#     print("Hello geek")

#18
#My choice is c. g and 10
#Ok

# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == "e" or letter == "s":
#             continue
#         print("Current letter :", letter)
#         var = 10
#         return var
#
# print(exercitiu(20))

#19
#a
#Ok

#20
#My choice is b
#Wrong. Argumentul optional lista is pastreaza valoarea de data trecuta cand a fost folosit ca argument optional
# def f(a, list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# # f(2, [1, 2, 3])
# f(2)

#21
#Index error
#Wrong, se returneaza lista goala
# list = ['1', '2', '3', '4', '5']
# print(list[12:])

#22
#a
#Ok
# class ClasaMea:
#     def Met1(self,a):
#         global var1
#         var1 = a
#
# obj=ClasaMea()
# obj.Met1("Salut Lume")

#23

# class Test123():
#     def __str__(self):
#         self.x = 77777
#         return str(self.x)
#
# obj_test123 = Test123()
# print(obj_test123)
#
# #24
# class X(object):
#     """Clasa adunare"""
#     def Ad(self, a, b, c):
#         return self.a + self.b + self.c
#
# obiect1=X()
# obiect1.Ad(1,2, 3)

#25

# class test123(object):
#     def rezultat(self):
#         self.y = 77777
#
# obj_test123=test123()
# obj_test123.rezultat()

#26
#Interpretorul nu va returna nimic si va crea obiectul
# class X(object):
#     def Ad():
#         print("Imi place python")
#
# obiect1=X()

#27
#Interpretorul returneaza eroare deoarece parametrul x pt init nu este gasit
# class Test123():
#     def __init__(self, x):
#         self.x = x
#
# obj_test123=Test123()

#28
# class Test123():
#     def __init__(self):
#         self.x = 77777
#
# obj_test123=Test123()
# print(obj_test123.x)

#29
#C. 0 metroda

#30
#b
# class Test1():
#     dynamic = "ceva"
#     def Met1(self):
#         return Test1.dynamic.upper()
#
# obj = Test1()
# obj.Met1()
# print(obj.Met1())

# string = "1 2 3 4 5 6 8 -12 9 20 31"

# list = string.split()
# print(list)
# def high_and_low(string):
#     list = string.split()
#     max_no = max(list)
#     min_no = min(list)
#     print(f"{max_no} {min_no}")
#     return None
#
# high_and_low("1 2 3 4 5 6 8 -12 9 20 31")






