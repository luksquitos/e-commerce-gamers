from rest_framework import viewsets
from products.models import Product
from products.api.serializers import ProductSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters



class ProductFilter(filters.FilterSet):
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    
    class Meta:
        model = Product
        fields = ["max_price", "min_price"]        


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend, 
        SearchFilter, 
        OrderingFilter
    ]
    filterset_class = ProductFilter
    search_fields = ["name"]
    ordering_fields = ["name", "price", "score"]
    http_method_names = ["get"]
    