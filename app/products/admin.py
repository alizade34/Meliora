from django.contrib import admin
from .models import Category, Product, ProductImage
    # Size, MaterialType, MetalType
# Register your models here.


admin.site.register(Category)
# admin.site.register(Size)
# admin.site.register(MaterialType)
# admin.site.register(MetalType)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]

# admin.site.register(ProductImage)

# class BasketAdmin(admin.ModelAdmin):
#     list_display = ['product', 'user', 'quantity']
#
# admin.site.register(Basket, BasketAdmin)