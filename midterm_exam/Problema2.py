# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:

def str_len2_combinations(dictionary):
    string_text = ""
    for i in dictionary.values():
        string_text += i
    lista_unica = sorted(list(set(string_text)))
    lista_combs = []
    for i in lista_unica:
        for j in lista_unica:
            if i != j:
                lista_combs.append(i+j)
    return lista_combs

# print(lista_combs)

dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}
print(str_len2_combinations(dictionar))


