# Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace
# battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.

def text_replacer(sentence, config_list, variator):
    """Functie care ia stringul si lista care contine intervalele de slice si textul inclouitor, si face inlocuirile
    Functia foloseste si un parametru variator care aranjeaza marginile intervalelor"""

    target_text = string[config_list[0] - 1 - variator:config_list[1] - variator:1]
    sentence_2 = sentence.replace(target_text, config_list[2])
    new_variator = variator + len(target_text) - len(config_list[2])
    return sentence_2, new_variator

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]

var = 0  #Definim o valoare initiala pentru variator.
# Acesta este un numar intreg care ajuta la ajustarea marginilor intervalului de slice
# pe masura ce se inlocuiesc cuvintele din cod. Asta ajuta cu diferentele de lungime intre textul de inlocuit si textul
# inlocuitor.

print(string)

for item in patches:
    result = text_replacer(string, item, var)
    string = result[0]
    var = result[1]

print(string)


