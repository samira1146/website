from django.db import models
from django.contrib.auth.models import User


class designer(models.Model):
    user = models.CharField(max_length=50)
    age = models.IntegerField()
    Work_Experience = models.IntegerField()

class jornal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()


class SignUp(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()







