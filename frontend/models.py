from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    price = models.DecimalField(max_length=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
