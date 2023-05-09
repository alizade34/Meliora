from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.


admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):

    class Meta:
        model = Product

    inlines = (ProductImageAdmin, )


admin.site.register(Product, ProductAdmin)

# class BasketAdmin(admin.ModelAdmin):
#     list_display = ['product', 'user', 'quantity']
#
# admin.site.register(Basket, BasketAdmin)