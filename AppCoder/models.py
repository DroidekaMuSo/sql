from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
