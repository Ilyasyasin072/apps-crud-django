from django.db import models


class Customers(models.Model):
    name_customers = models.CharField(max_length=50)
    address_customers = models.TextField()
    phone = models.IntegerField()

    class Meta:
        db_table = 'customers'
