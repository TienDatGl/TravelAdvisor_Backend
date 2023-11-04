from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    class Meta:
        unique_together = ('name', 'category')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False)
    image = models.ImageField(upload_to='places/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', blank=True, null=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=255, null=False)
    days = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
    

class TripItem(models.Model):
    day = models.DateField(null=False)
    locations = models.ManyToManyField('Location', blank=True, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE,  related_name='items', default=None)

    # def __str__(self) -> str:
    #     return self.day


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)

