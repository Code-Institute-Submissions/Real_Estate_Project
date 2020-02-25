from django.db import models
from signup.models import Signup


class Payment(models.Model):
    full_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=15, blank=False)
    city = models.CharField(max_length=30, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    payment = models.ForeignKey(Payment, null=False)
    signup = models.ForeignKey(Signup, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.signup.name, self.signup.price)
