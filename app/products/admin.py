from django.contrib import admin
from products.models import Product
from django.utils.safestring import mark_safe



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "score", "quantity"]
    list_display_links = ["name"]
    readonly_fields = ["image_preview"]
    search_fields = ["id", "name"]

    @admin.display(description="Preview da imagem")
    def image_preview(self, obj):
        url = obj.image.url
        width = obj.image.width
        height = obj.image.height
        image = "<img src='%s' width='%f' height='%f'/>"
        
        if width > 300 and height > 300:
            return mark_safe(image % (url, width * 0.65, height * 0.65))
        
        return mark_safe(image % (url, width, height))