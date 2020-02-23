from django.db import models


# Create your models here.


class Payment(models.Model):
    full_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=15, blank=False)
    city = models.CharField(max_length=30, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


