from django.contrib import admin
from costumers.models import Costumer, Purchase, PurchaseProduct


#FIXME
# Encontrar uma forma de impedir que o superuser
# criado por alguém consiga adicionar 
# qualquer um destes. 

class PurchaseProductInline(admin.StackedInline):
    model = PurchaseProduct
    extra = 0
    readonly_fields = ["product"]
    

class PurchaseInline(admin.StackedInline):
    model = Purchase
    extra = 0
    readonly_fields = [
        "id", 
        "received", 
        "costumer", 
        "date_time_purchase", 
        "date_time_received"
    ]


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "name", "email"]
    inlines = [PurchaseInline]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id", 
        "received", 
        "costumer", 
        "date_time_purchase", 
        "date_time_received"
    ]
    inlines = [PurchaseProductInline]
    
