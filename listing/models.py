from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Listing(models.Model):
    '''model to add properties'''

    bool = ((True, 'Yes'), (False, 'No'))
        
    title = models.CharField(max_length=50)
    buy = models.BooleanField(choices=bool)
    rent = models.BooleanField(choices=bool)    
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    rooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0) 
    garage = models.BooleanField(choices=bool)
    garden = models.BooleanField(choices=bool)
    # image
    photos = models.ImageField(upload_to="img", default="photo")
    photo1 = models.ImageField(upload_to="img", default="img1")
    photo2 = models.ImageField(upload_to="img", default="img2")
    # textarea
    description = models.TextField(max_length=1000)
    # time Posted time.zone
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.id, self.title, self.user)