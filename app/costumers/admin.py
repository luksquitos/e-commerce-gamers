from django.contrib import admin
from costumers.models import Costumer, Purchase, PurchaseProduct


class AdminNoPermissionsMixin:
    """
    This mixin removes the 
    permissions of a Admin class
    """
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class PurchaseProductInline(AdminNoPermissionsMixin, admin.StackedInline):
    model = PurchaseProduct
    extra = 0
    
    
class PurchaseInline(AdminNoPermissionsMixin, admin.StackedInline):
    model = Purchase
    extra = 0
    readonly_fields = ["date_time_purchase"]




@admin.register(Costumer)
class CostumerAdmin(AdminNoPermissionsMixin, admin.ModelAdmin):
    list_display = ["id", "name", "amount_purchases"]
    list_display_links = ["name"]
    inlines = [PurchaseInline]

    @admin.display(description="Quantidade de compras")
    def amount_purchases(self, obj):
        purchases = Purchase.objects.filter(costumer=obj)
        return purchases.count()


@admin.register(Purchase)
class PurchaseAdmin(AdminNoPermissionsMixin, admin.ModelAdmin):
    readonly_fields = ["date_time_purchase"]
    inlines = [PurchaseProductInline]
    
