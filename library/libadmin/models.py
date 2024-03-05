from django.db import models
# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    discription=models.TextField(max_length=50)
    
    def __str__(self):
        return self.name