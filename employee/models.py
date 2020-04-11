from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
