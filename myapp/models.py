from django.db import models
from seller.models import *

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=150)
    address = models.TextField()
    pic = models.FileField(upload_to='profile_pics', default='sad.png')

    def __str__(self):
        return self.email


class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)