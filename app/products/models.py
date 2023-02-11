from django.db import models


class Product(models.Model):
    name = models.CharField("Nome do produto", max_length=300)
    price = models.DecimalField("Preço", max_digits=5, decimal_places=2)
    description = models.TextField("Descrição", blank=True)
    score = models.PositiveSmallIntegerField("Pontuação")
    quantity = models.PositiveSmallIntegerField("Quantidade", help_text="estoque")
    image = models.ImageField("Imagem", upload_to="product-image", blank=True)

    # A quantidade disponível não pode ser uma property
    # porque como que iria funcionar a reposição do 
    # estoque ?
    # Assim que uma compra for realizada
    # um número deverá ser tirado
    # do total. 
    
    @property
    def is_available(self):
        return self.quantity > 0
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]