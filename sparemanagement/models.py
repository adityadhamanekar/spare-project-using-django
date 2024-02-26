from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplierName = models.CharField(max_length= 20)
    province = models.CharField(max_length= 20)
    city = models.CharField(max_length= 20)
    phone_number = models.CharField(max_length=10, unique=True)


class Employee(models.Model):
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    gender= models.CharField(max_length= 10)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique = True)
    role = models.CharField( max_length=20)
