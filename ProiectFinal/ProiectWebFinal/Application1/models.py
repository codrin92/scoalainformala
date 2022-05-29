from django.db import models

# Create your models here.

class Reporting(models.Model):

    project_name = models.CharField(max_length=100)
    project_address = models.CharField(max_length=300)
    project_value=models.BigIntegerField(default=0)
    client=models.CharField(max_length=50)
    building_height=models.BigIntegerField(default=0)
    building_type=models.CharField(max_length=50)
    number_of_stairs=models.BigIntegerField(default=0)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.project_name}"


