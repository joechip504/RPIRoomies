from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    """ Stores first/last name, facebook id """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fid = models.CharField(max_length=100)

    # def __eq__(self, other):
    	# return self.fid == other.fid
