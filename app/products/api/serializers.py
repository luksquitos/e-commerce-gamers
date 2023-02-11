from rest_framework import serializers
from products.models import Product



#FIXME
# O atributo quantity que será entregue para 
# o viewset será a property com a quantidade 
# restante

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"