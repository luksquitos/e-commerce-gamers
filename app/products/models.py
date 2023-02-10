from django.db import models


class Product(models.Model):
    name = models.CharField("Nome do produto", max_length=300)
    price = models.DecimalField("Preço", max_digits=5, decimal_places=2)
    description = models.TextField("Descrição", blank=True)
    score = models.PositiveSmallIntegerField("Pontuação")
    quantity = models.PositiveSmallIntegerField("Quantidade", help_text="estoque")
    image = models.ImageField("Imagem", upload_to="product-image", blank=True)

    #TODO 
    # Property que retorna quantidade 
    # mínima para venda.
    @property
    def available_quantity(self):
        """
        Quantity available for sale.
        """
        ...
    available_quantity.fget.short_description = "Quantidade disponível"