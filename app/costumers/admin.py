from django.contrib import admin
from costumers.models import Costumer, Purchase, PurchaseProduct


class AdminNoPermissionsMixin:
    """
    This mixin removes the 
    permissions of a Admin class
    """
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request):
        return False
    
    def has_delete_permission(self, request):
        return False


class PurchaseProductInline(AdminNoPermissionsMixin, admin.StackedInline):
    model = PurchaseProduct
    extra = 0
    
    
class PurchaseInline(AdminNoPermissionsMixin, admin.StackedInline):
    model = Purchase
    extra = 0




@admin.register(Costumer)
class CostumerAdmin(AdminNoPermissionsMixin, admin.ModelAdmin):
    inlines = [PurchaseInline]


@admin.register(Purchase)
class PurchaseAdmin(AdminNoPermissionsMixin, admin.ModelAdmin):
    inlines = [PurchaseProductInline]
    
