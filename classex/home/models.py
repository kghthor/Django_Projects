from django.db import models

# Create your models here.
class Information(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=25,unique=True)
    mobile=models.CharField(max_length=10,unique=True)
    

    def __str__(self):
        return self.name