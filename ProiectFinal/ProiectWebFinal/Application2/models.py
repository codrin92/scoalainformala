# from datetime import date
#
# from django.db import models
#
# from Application1.models import Reporting
#
# class Revenues(models.Model):
#     name = models.CharField(max_length=20, default='abc')
#     reporting = models.ForeignKey(Reporting, on_delete=models.CASCADE)
#     # project_id = models.ForeignKey(Reporting, on_delete=models.CASCADE)
#     # project_name = models.CharField(max_length=100)
#     # project_address = models.CharField(max_length=300)
#     # project_value = models.BigIntegerField(default=0)
#     # client_company = models.CharField(max_length=50)
#     # client_representative = models.CharField(max_length=100)
#     # building_height = models.BigIntegerField(default=0)
#     # building_type = models.CharField(max_length=50)
#     # number_of_stairs = models.BigIntegerField(default=0)
#     # active = models.BooleanField(default=1)
#     # quote_produced = models.BooleanField(default=0)
#     # quote_issued = models.BooleanField(default=0)
#     # quote_accepted = models.BooleanField(default=0)
#     # report_generated = models.BooleanField(default=0)
#     # request_date = models.CharField(default=str(date.today()), max_length=100)
#     # project_fee = models.CharField(default='NA', max_length=10)
#     # project_name = models.OneToOneField(Reporting, on_delete=models.CASCADE, primary_key=True)
#
#     # profile_pic = models.ImageField(upload_to=user_directory_path, null=True, blank=True) pentru poze
#     # profile_pic = models.ImageField(upload_to=‘ / covers’, null = True, blank = True)
#
#     def __str__(self):
#         return f"{self.name}"
#
# # Create your models here.
