from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from costumers.models import Costumer, Purchase
from costumers.api.serializers import CostumerSerializer, PurchaseSerializer
from products.models import Product



class CostumerViewset(viewsets.ModelViewSet):
    serializer_class = CostumerSerializer
    queryset = Costumer.objects.all()


class PurchaseViewset(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    permission_classes = [IsAuthenticated]
    
    #FIXME
    # Essa função deve retornar apenas as compras
    # do usuário autenticado
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    @action(detail=False, methods=["post"])
    def post_cart(self, request):
        """
        Essa action é para receber o carrinho que
        foi armazenado no navegador do cliente 
        """
        costumer = Costumer.objects.get(user=request.user)
        products_in_cart = request.data.get('products')
        products_unavailable = self.all_products_available(products_in_cart)
        
        if isinstance(products_unavailable, list):
            msg = (
                "Unable to finish your order."
                "The following items are unavailable"
            )
            return Response(
                data={
                    "msg": msg,
                    "products": products_unavailable
                },
                status=400
            )


        new_purchase = Purchase.objects.create(
            received=False, 
            costumer=costumer,
            address=costumer.address
        )
        deliver = 0
        purchase_price = 0

        for product_dict in products_in_cart:
            product = Product.objects.get(
                pk=product_dict.get('product')
            )
            quantity = product_dict.get('quantity')
            purchase_price += new_purchase.create_product_by_quantity(product, quantity)
            deliver *= 10 * quantity
        
        # Updating the blank values
        new_purchase.purchase_price = purchase_price
        new_purchase.deliver = deliver if purchase_price < 250 else 0
        new_purchase.save()
        
        msg = (
            "Compra realizada"
            f"O total foi de R${new_purchase.purchase_price} reais"
            f"Frete: {new_purchase.deliver}"
        )
        
        return Response({"msg": msg}, status=200)



    def all_products_available(self, products_in_cart: dict):
        products_unavailable = []
        
        for product_dict in products_in_cart:
            product = Product.objects.get(
                pk=product_dict.get('product')
            )
        
            if not product.quantity >= product_dict.get('quantity'):
                data = {
                    "id": product.id,
                    "name": product.name
                }
                products_unavailable.append(data)
        
        if len(products_unavailable) > 0:
            return products_unavailable
        else:
            return True
            