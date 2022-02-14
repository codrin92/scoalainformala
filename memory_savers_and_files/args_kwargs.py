# def my_function(param_1):
#     return param_1
#
#
# print(my_function('string'))
#
# def my_function_2(*param_1):  # *ne permite sa introducem un numar nedefinit de parametri
#     print(type(param_1))
#     return param_1
#
#
# print(my_function_2('string', 'string1', 'string2'))
#
# def numbers_sum(*var):
#     suma = 0
#     print(var)
#     for item in var:
#         suma = suma + item
#     return suma
#
# print(numbers_sum(1, 2, 3, 4, 5))

# def numbers_sum(param_1, *var):    #Parametrul stelat trebuie sa fie mereu la final
#     suma = 0
#     print(var)
#     for item in var:
#         suma = suma + item
#     return suma
#
#
# print(numbers_sum(1, 2, 3, 4, 5, 1))

def catalog(**kwargs):   #** este de tip dictionar. Putem folosi si *args si **kwargs dar doar in aceasta ordine
    print(type(kwargs))
    return kwargs.keys()

print(catalog(nume="Popa", prenume = "Ionut", varsta = "12"))