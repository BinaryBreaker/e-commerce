from django.db import models


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200)
    Picture = models.ImageField(upload_to="Category")
    Active = models.BooleanField()

    def __str__(self):
        return self.Name


class Product(models.Model):
    title = models.CharField(max_length=500)
    Price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=300)
    tags = models.CharField(max_length=500)
    sizes = models.CharField(max_length=500,null=True)
    colors = models.CharField(max_length=500,null=True)
    Stock = models.IntegerField()

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    image = models.ImageField(upload_to="Product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
