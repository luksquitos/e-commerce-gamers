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
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Returns only Purchases 
        from a specific user.
        """
        qs = Purchase.objects.filter(
            costumer__user=self.request.user
        )
        return qs
    

    @action(detail=False, methods=["post"])
    def post_cart(self, request):
        """
        This action will receive the cart 
        from the Client Browser and process
        the order.
        If the products are unavailable, 
        the order won't be processed.
        """
        costumer = Costumer.objects.get(user=request.user)
        products_in_cart = request.data.get('products')
        products_unavailable = self.all_products_available(products_in_cart)
        
        if isinstance(products_unavailable, list):
            msg = (
                "Não foi possível finalizar seu pedido. "
                "Os itens a seguir estão indisponíveis."
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
        deliver = 1
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
            "Compra realizada. "
            f"O total foi de R${new_purchase.purchase_price} reais. "
            f"Frete: R${new_purchase.deliver} reais"
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
            