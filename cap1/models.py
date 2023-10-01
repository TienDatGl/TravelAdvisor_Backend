from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True)



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
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    image = models.ImageField(upload_to='places/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', blank=True, null=True)


class Trip(models.Model):
    name = models.CharField(max_length=255, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    days = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)


class Favorite(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)