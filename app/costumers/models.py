from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField("Nome", max_length=100)
    email = models.EmailField("Email")
    address = models.CharField("Endereço", max_length=400)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Purchase(models.Model):
    received = models.BooleanField("Compra entregue?")
    costumer = models.ForeignKey(Costumer, on_delete=models.DO_NOTHING)
    date_time_purchase = models.DateTimeField("Data e hora de compra", auto_now_add=True)
    date_time_received = models.DateTimeField("Data e hora de recebimento", null=True)
    
    def __str__(self) -> str:
        string = (
            f"Compra {self.id} - {self.costumer.name}"
        )
        return string
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"    
    

class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="products")
    
    #TODO
    # O método save será sobrescrito para 
    # tratar a quantidade do Product ?
    # melhor ser pelo viewset
    

