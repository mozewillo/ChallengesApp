from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField(default=datetime.now)
    duration = models.IntegerField()
    counter = models.IntegerField('completed', default=0)
    version = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, default=1)