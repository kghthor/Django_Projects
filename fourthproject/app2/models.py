from django.db import models
# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    gender=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)