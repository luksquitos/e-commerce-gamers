from rest_framework import viewsets
from costumers.models import Costumer, Purchase
from costumers.api.serializers import CostumerSerializer, PurchaseSerializer
from rest_framework.permissions import IsAuthenticated


class CostumerViewset(viewsets.ModelViewSet):
    serializer_class = CostumerSerializer
    queryset = Costumer.objects.all()


class PurchaseViewset(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    # permission_classes = [IsAuthenticated]
    
    #FIXME
    # Essa função deve retornar apenas as compras
    # do usuário autenticado
    
    def get_queryset(self):
        return super().get_queryset()
    
    