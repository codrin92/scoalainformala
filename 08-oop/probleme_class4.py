# 2. Creati o clasa care se numeste lista_CD_DVD.
# La crearea unui obiect ala cestei clase va solicita doua argumente reprezentand titlu si
# continut cu care va crea doua atribute.
# Fiecare obiect creat va fi adaugat intr-o lista din namespace-ul global Clasa are o
# metoda care cauta si gaseste pe baza textului dat ca argument un obiect, afisiand titlu
# si continutul. Se va folosi lista de obiecte pentru a cauta.
# La afisarea obiectului returnati utilizand metoda __str__ titlul obiectului.
# Aplicati clasa pentru 3 exemple apoi folositi cautarea pe un caz pozitiv si unul
# negativ. Printati cele 3 obiecte.

class Lista_CD_DVD:
    lista_obj = []
    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        self.lista_obj.append([self.titlu, self.continut])

    @staticmethod
    def cautare(argument):
        msg = f"Obiectul nu a fost gasit"
        for i in Lista_CD_DVD.lista_obj:
            if argument in i[0] or argument in i[1]:
                msg = f"Obiectul cautat este Titlu: {i[0]} Continut: {i[1]}"
        return msg

    def __str__(self):
        return f"Titlul este {self.titlu}"

dvd1 = Lista_CD_DVD("Grand Theft Auto", "Game")
dvd2 = Lista_CD_DVD("Avatar", "Film pe care nu l-am vazut")
cd1 = Lista_CD_DVD("Bitdefender", "Antivirus")

print(cd1)
print(Lista_CD_DVD.cautare("virus"))
print(Lista_CD_DVD.cautare("NFS"))

# 3. Creati un program ce are o clasa numita util. Clasa are o variabila a clasei de tip lista
# populata automat in constructor(__init__) cu obiectul.
# Creati a doua clasa numita izatori care primeste in constructor doua argumente numite
# user si passw, formand cu ajutorul acestora doua atribute cu acelasi nume.
# Creati a treia clasa numita utilizatori care sa mosteneasca clasele util și izatori fără a
# pierde din functionalitatea claselor mostenite.
# De asemenea, aceasta clasa are o metoda privata numita parole care sa returneze un
# set cu toate parolele și o metoda privata numita useri care sa returneze un set cu toți
# userii. Se va folosi variabila clasei de tip lista care are toate obiectele pentru căutare.
# Interpretorul trebuie sa ridice o eroare setata de voi în cazul în care este apelat
# obiectul prin len(). Setati 3 obiecte și testați functionalitatea.

# class Util:
#     lista_obj = []
#     def __init__(self):
#         self.lista_obj.append(self)
#
#     def __str__(self):
#         return f"{self.lista_obj}"
#
# class Izatori():
#     def __init__(self, user, passw):
#         self.user = user
#         self.passw = passw
#
# class Utilizatori(Util, Izatori):
#     set_parole = set()
#     set_useri = set()
#
#     def __init__(self, user, passw):
#         Util.__init__(self)
#         Izatori.__init__(self, user, passw)
#
#     @staticmethod
#     def __parole():
#         for i in Utilizatori.lista_obj:
#             Utilizatori.set_parole.add(i.passw)
#         return f"Lista de parole este: {Utilizatori.set_parole}"
#
# om_bun = Utilizatori("pisici", "catei")
# om_bun2 = Utilizatori("pisicile", "cateii")
# om_bun4 = Utilizatori("dinozauri", "balauri")
#
# print(Utilizatori.lista_obj)
# print(om_bun.user)
#
# print(Utilizatori.__dict__)
#
# print(_Util__parole())

#Rezolvare Alexandra

