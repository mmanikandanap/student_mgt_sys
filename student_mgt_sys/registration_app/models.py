from django.db import models


# Create your models here.
class Datas(models.Model):
  Name=models.CharField(max_length=20,default="")
  Age=models.IntegerField(max_length=20,default="")
  Sex=models.CharField(max_length=10,default="")
  Standard=models.IntegerField(max_length=20,default="")
  Percentage=models.FloatField(max_length=10,default="")
  Address=models.CharField(max_length=250,default="")