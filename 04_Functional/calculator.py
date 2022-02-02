# 2 variabile
# 1 operator
# 1 rezultat

def suma(a: int, b: int) -> str:
    return f"{a} + {b} = {a + b}"

def diferenta(a: int, b: int) -> str:
    return f"{a} - {b} = {a - b}"

def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} = {a * b}"

def impartire(a: int, b: int) -> str:
    if b ==0:
        while b == 0:
            b = int(input("Aloca o noua valoare pentru b: "))
    if a % b == 0:
        c = int (a / b)
    else:
        c = float (a / b)
    return f"{a} / {b} = {c}"
#o functie trebuie sa aiba un singur return

def operator() -> str:
    op = input("Alege operatorul: ")
    if op not in ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op = input("Alege operatorul: ")
    return op  #Important, o data ce functia ajunge la un return, se iese din functie

def conversie(mesaj_input: str):
    nr = input(f"{mesaj_input}")
    while nr.isdigit() is False:
        nr = input(f"{mesaj_input}")
    return int(nr)


def calculator():

    nr1 = conversie("Primul numar: ")
    nr2 = conversie("Al doilea numar: ")
    op = operator()
    if op == '+':
        rezultat = suma(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat

def calculator_cu_eval():

    nr1 = conversie("Primul numar: ")
    nr2 = conversie("Al doilea numar: ")
    op = operator()
    # if op == '+':
    #     rezultat = suma(nr1, nr2)
    # elif op == '-':
    #     rezultat = diferenta(nr1, nr2)
    # elif op == '*':
    #     rezultat = inmultire(nr1, nr2)
    # else:
    #     rezultat = impartire(nr1, nr2)
    return f"{nr1} {op} {nr2} =", eval(f"{nr1} {op} {nr2}")

#Functia eval ne ajuta sa evitam multe operatii cu string in programare



# print(calculator())

print(calculator_cu_eval())