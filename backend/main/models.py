from django.db import models


class Event(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
