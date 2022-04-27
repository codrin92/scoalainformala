from django.db import models

# Create your models here.
# Comanda pentru activare env: .\env\Scripts\activate

company_choices = (("SRL", "S.R.L."), ("SA", "S.A."))


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)  # Text field e mai mare decat CharField
    company_type = models.CharField(max_length=10, choices=company_choices)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} - {self.company_type}"