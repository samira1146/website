from django.db import models
from django.contrib.auth.models import User


class Designer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    work_experience = models.IntegerField()

class Jornal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()


# class SignUp(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     age = models.IntegerField()







