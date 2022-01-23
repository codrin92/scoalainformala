# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
# ● Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n]
# ● Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.

def your_function(*args,**kwargs):
    # args=[1, 5, -3, 'abc', [12, 56, 'cad'], 48, -20]
    sum=0
    dims=len(args)
    for i in range(dims):
        if isinstance(args[i], int)==True:
            sum=sum+args[i]
    print(sum)

your_function(1, 5, -3, 'abc', [12, 56, 'cad'], 48, -20, param_3=2)

# Functie recursiva
def rec_sum(s):
    if isinstance(s, int)==False:
        return 0
    elif s<1:
        return 0
    else:
        return s+rec_sum(s-1)

print(rec_sum(1))

# Functie recursiva - suma nr pare
def rec_sum(s):
    if isinstance(s, int)==False:
        return 0
    elif s<1:
        return 0
    else:
        if s%2==0:
            return s+rec_sum(s-1)
        else:
            return s-1+rec_sum(s-2)

print(rec_sum())

# Functie recursiva - suma nr impare
def rec_sum(s):
    if isinstance(s, int)==False:
        return 0
    elif s<1:
        return 0
    else:
        if s%2!=0:
            return s+rec_sum(s-1)
        else:
            return s-1+rec_sum(s-2)

print(rec_sum(6))

# Functie care citeste valoarea si o returneaza daca este nr intreg. Returneaza 0 daca nu
def input_function():
    c=input("Please provide a number: ")
    try:
        my_int=int(c)
        print(c)
    except ValueError:
        print('0')

input_function()



