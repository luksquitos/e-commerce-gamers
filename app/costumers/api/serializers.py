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
        fields = ["product"]
        depth = 1

 
class PurchaseSerializer(serializers.ModelSerializer):
    products = PurchaseProductSerializer(read_only=True, many=True)
    
    def update(self, instance, validated_data):
        from datetime import datetime
        current_time = datetime.now()
        
        instance.received = validated_data.get('received')
        instance.date_time_received = current_time
        instance.save()
        
        return instance
    
    class Meta:
        model = Purchase
        fields = "__all__"
