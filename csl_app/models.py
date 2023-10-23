from django.db import models

from django.db import models



class TypeCategory(models.Model):
    name= models.CharField(max_length=80)

    def __str__(self):
        return self.name

class ProductStatus(models.Model):
    name=models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Users(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    photo = models.ImageField(upload_to='imagenes/')
    email=models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    status_sale = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='imagenes/')
    category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE)


class HistoryProductSale(models.Model):
    date_sale = models.DateField()
    product_sale = models.ForeignKey(Product, on_delete=models.CASCADE)

class HistoryProductBuy(models.Model):
    date_buy = models.DateField()
    product_buy = models.ForeignKey(Product, on_delete=models.CASCADE)


