# 2. Se da urmatoarea lista:
# lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’,
# ‘Claudiu’]
# Se cere:
# 1. Sortati lista dupa nume
# 2. Determinati numarul de aparitii al fiecarui nume
# 3. Listati numele care apare de cele mai multe ori in lista initiala.
# 4. Listati numele care apare de cele mai putine ori in lista initiala.

lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

lista_sortata = sorted(lista_nume)
set_de_nume = set(lista_sortata)

dict = {}

for nume in set_de_nume:
    counter = 0
    for i in lista_nume:
        if nume == i:
            counter += 1
    dict[nume] = counter

# list(dict.fromkeys(lista)) - returneaza doar valorile unice dintr-o lista, in ordinea initiala


max_key = max(dict, key=dict.get)
max_no = max(dict.values())
min_key = min(dict, key=dict.get)
min_no = min(dict.values())

print(f"Aceasta este lista sortata de nume: {lista_sortata}")
print(f"Frecventa numelor in lista initiala este urmatoarea : {dict}")

print(f"Numele cel mai frecvent este {max_key} cu un numar total de {max_no} aparitii")
print(f"Numele cel mai putin frecvent este {min_key} cu un numar total de {min_no} aparitii")

#Palindrom
# def is_palindrome(string: str)
# def palindrome_sentence(sentence: str) -> bool:
#     """
#     Check if a sentence is a palindrome.
#
#     The function ignores whitespace, capitalisation and
#     punctuation in the sentence.
#
#     :param sentence: The sentence to check.
#     :return: True if `sentence` is a palindrome, False otherwise.
#     """
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return is_palindrome(string)

def generatePermutation(string, start, end):
    current = 0
    # Prints the permutations
    if (start == end - 1):
        print(string)
    else:
        for current in range(start, end):
            # Swapping the string by fixing a character
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            # Recursively calling function generatePermutation() for rest of the characters
            generatePermutation("".join(x), start + 1, end)
            # Swapping the string by fixing a character
            temp = x[start]
            x[start] = x[current]
            x[current] = temp


str = "ABCDEF"
n = len(str)
print("All the permutations of the string are: ")
generatePermutation(str, 0, n)





