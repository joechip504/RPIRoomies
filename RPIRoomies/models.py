from django.db import models

# Create your models here.

class Person(models.Model):
    fid = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

