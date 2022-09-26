from email.headerregistry import Address
from django.db import models

# Create your models here.
class Services(models.Model):
    Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Brand(models.Model):

    Name_Brand= models.CharField(max_length=100)
    Address_Brand=models.CharField(max_length=100)
    Date_service=models.DateField()
    software_service=models.ForeignKey(Services,on_delete=models.CASCADE)
