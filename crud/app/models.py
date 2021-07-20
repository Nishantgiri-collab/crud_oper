from django.db import models

# Create your models here.
class Product(models.Model):
    Date=models.DateField(null=True)
    Provider = models.CharField(max_length=100)
    Name_of_product = models.CharField(max_length=100)
    Price = models.FloatField()
    Quality = models.IntegerField()
    Amount = models.FloatField()
    Stock = models.IntegerField()

