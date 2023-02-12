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
    purchase_price = models.DecimalField("Preço da compra", max_digits=8, decimal_places=2, null=True)
    deliver = models.DecimalField("Frete", max_digits=4, decimal_places=2, null=True)
    address = models.CharField("Endereço de entrega", max_length=400, null=True)
    date_time_purchase = models.DateTimeField("Data e hora de compra", auto_now_add=True)
    date_time_received = models.DateTimeField("Data e hora de recebimento", null=True)
    
    def __str__(self) -> str:
        string = (
            f"Compra {self.id} - {self.costumer.name}"
        )
        return string
    
    
    def create_product_by_quantity(self, product, quantity: int):
        """
        This function is used by 'post_cart' action,
        in purchase viewset, so it can create
        multiple instances of a product for the 
        same purchase.
        And subtract 1 from the total in stock.
        Returns the total.
        """
        products_price = 0
        
        for _ in range(quantity):
            self.products.create(
                product=product
            )
            product.quantity -= 1
            product.save()
            products_price += product.price
        
        return products_price
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"    
    

class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
