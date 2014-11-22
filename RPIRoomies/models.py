from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    fid = models.CharField(max_length=50)
    user = models.OneToOneField(User)
    #friends = models.ManyToManyField('self')

