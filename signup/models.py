from django.db import models


# Create your models here.

class Signup(models.Model):
    
    name = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
