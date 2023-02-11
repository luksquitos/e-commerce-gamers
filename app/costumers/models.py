from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=100)


class Purchase(models.Model):
    received = models.BooleanField("Compra entregue?")
    costumer = models.ForeignKey(Costumer, on_delete=models.DO_NOTHING)
    date_time_purchase = models.DateTimeField("Data e hora de compra", auto_now_add=True)
    

class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    
    #TODO
    # O método save será sobrescrito para 
    # tratar a quantidade presente?
    # melhor ser pelo viewset
    

