from django.db import models


class Buy_package(models.Model):

    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    total = models.ImageField(blank=False)
