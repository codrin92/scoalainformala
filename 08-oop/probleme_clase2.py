class CatalogAuto:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def schimbare_culoare(self, culoare):
        self.culoare = culoare

    def __str__(self):
        return f"Culoarea este: {self.culoare}"

class ScauneIncalzite(CatalogAuto):
    def __init__(self, scaune_incalzite, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite

    def __str__(self):
        return f"Marca este {self.marca}, tipul este {self.tip}. Scaune incalzite: {self.scaune_incalzite}"

class BlocuriOptice(CatalogAuto):
    def __init__(self, blocuri_optice, marca, tip):
        super().__init__(marca, tip)
        self.blocuri_optice = blocuri_optice

    def __str__(self):
        return f"Marca este {self.marca}, tipul este {self.tip}. Blocuri optice: {self.blocuri_optice}"

obj = ScauneIncalzite("Nu", "Aro", "461")
print(obj)
obj.schimbare_culoare("Rosu")
print(obj.culoare)

obj2 = BlocuriOptice(marca="Dacia", tip = "1310", blocuri_optice="Nu")
print(obj2)
obj2.schimbare_culoare("negru")
print(obj2.culoare)

