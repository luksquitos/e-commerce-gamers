from rest_framework import serializers
from django.contrib.auth.models import User
from costumers.models import Costumer, Purchase, PurchaseProduct


class CostumerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.get('email')
        
        user = User.objects.create(username=email)
        user.set_password(password)
        user.save()
        
        costumer = Costumer.objects.create(
            user=user, **validated_data
        )
        return costumer

    class Meta:
        model = Costumer
        exclude = ("user",)
        

class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseProduct
        fields = "__all__"

#TODO
# Criar outros atributos para valor da compra
# quando os dados forem retornados. 
class PurchaseSerializer(serializers.ModelSerializer):
    products = PurchaseProductSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = "__all__"
