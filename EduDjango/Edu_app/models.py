from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=300, null=True)
    age=models.CharField(max_length=300, null=True)
    dateofbirth=models.DateTimeField(max_length=300, null=True)
    def __str__(self):
        return self.name

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name='streams')

    def __str__(self):
        return self.name


    