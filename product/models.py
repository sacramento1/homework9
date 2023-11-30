from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField (blank=False, null=False)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False, blank=False)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)
    image = models.ImageField(default='images/default_product.jpg')

    def __str__(self) -> str:
        return self.name
