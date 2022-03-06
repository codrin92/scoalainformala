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
max_key = max(dict, key=dict.get)
max_no = max(dict.values())
min_key = min(dict, key=dict.get)
min_no = min(dict.values())

print(f"Aceasta este lista sortata de nume: {lista_sortata}")
print(f"Frecventa numelor in lista initiala este urmatoarea : {dict}")

print(f"Numele cel mai frecvent este {max_key} cu un numar total de {max_no} aparitii")
print(f"Numele cel mai putin frecvent este {min_key} cu un numar total de {min_no} aparitii")





