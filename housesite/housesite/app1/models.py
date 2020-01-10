from django.db import models


# Create your models here.
class product(models.Model):
    img = models.ImageField(upload_to='images')
    price = models.IntegerField()
    name = models.CharField(max_length=500)
    desc = models.TextField(max_length=500)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name


class profile(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=500)
    desc = models.TextField(max_length=500)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class newss(models.Model):
    img = models.ImageField(upload_to='images')
    date = models.DateField()
    name = models.CharField(max_length=500)
    desc = models.TextField(max_length=500)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
