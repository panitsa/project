from django.db import models

# Create your models here.
class Representative(models.Model):
    image = models.ImageField(upload_to='Representative_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    

class Activity_news(models.Model):
    image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    text = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    

class Villagepublic(models.Model):
    image = models.ImageField(upload_to='Villagepublic_images/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
