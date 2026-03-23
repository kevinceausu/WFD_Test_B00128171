from django.db import models


class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
