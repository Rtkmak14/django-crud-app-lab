from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Beer(models.Model):
    name=models.CharField(max_length=100)
    brewery=models.CharField(max_length=100)
    style=models.CharField(max_length=100)
    notes=models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("beer-detail", kwargs={"beer_id": self.id})

class Tasting(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    beer= models.ForeignKey(Beer,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('beer-detail', kwargs={'beer_id': self.beer.id})
    


