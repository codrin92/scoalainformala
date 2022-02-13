#Se importa tot modulul
import primul_nostru_modul

#Sau daca vrem sa importam doar o functie
from primul_nostru_modul import my_sum as suma #se pot redenumi pachetele in namespaceul local

# import math
# from math import sum

# sum()

if __name__ == '__main__':
    # print(primul_nostru_modul.my_sum(1, 4))
    print(suma(5, 4))

#Un pachet contine mai multe module.

#Nu se pot importa pachete care incep cu cifra