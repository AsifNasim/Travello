from django.db import models

# Create your models here.

class Destination(models.Model): # when you want to convert your class into model so that it can create tables in DB
    # id: int # in database it is automatically gets created when we create table so we dont have to explcitly declare here
    name= models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default = False)