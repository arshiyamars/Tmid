from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)  # Fixed typo: CharField instead of Charfield
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #description = models.TextField()  # Fixed typo: TextField instead of Textfield
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Textarea (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


class Textarea1 (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


class slider1 (models.Model):
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
class slider2 (models.Model):
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name