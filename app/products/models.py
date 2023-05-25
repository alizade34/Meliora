from django.db import models
from services.mixins import DateMixin
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from services.uploader import Uploader

User = get_user_model()


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel, DateMixin):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

class Size(MPTTModel, DateMixin):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self) -> str:
        return self.name

class MetalType(MPTTModel, DateMixin):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

class MaterialType(MPTTModel, DateMixin):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name


class AA(MPTTModel, DateMixin):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name


class Product(DateMixin):
    COLOR_CHOICES = [
        ('R', 'Red'),
        ('G', 'Green'),
        ('B', 'Blue'),
        ('W', 'White'),
        ('WG', 'White Gold'),
        ('P', 'Pink'),
        ('PP', 'Purple'),
        ('O', 'Orange'),
        ('BW', 'Brown'),
        ('B', 'Blue'),
        ('Y', 'Yellow'),
        ('YG', 'Yellow Gold'),
        ('M', 'Mix'),
        ('GR', 'Grey'),
        ('BB', 'Black'),
    ]

    PROMOTION_CHOICES = [
        ('on sale', 'on sale'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    metal_type = models.ForeignKey(MetalType, on_delete=models.CASCADE, blank=True, null=True)
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300)
    description = RichTextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    type = models.CharField(blank=True, max_length=300)
    color = models.CharField(blank=True, max_length=300, choices=COLOR_CHOICES)
    promotion = models.CharField(blank=True, max_length=300, choices=PROMOTION_CHOICES)
    wishlist = models.ManyToManyField(User, blank=True, related_name='product_wishlist')


    def __str__(self) -> str:
        return self.name


class ProductImage(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=Uploader.upload_image_to_product)
    def __str__(self) -> str:
        return self.product.name








# class Basket(DateMixin):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#
#     def __str__(self):
#         return f"{self.user.email} --> {self.user.name}"
#
#     class Meta:
#         ordering = ('-created_at', )
#         verbose_name = 'Basket'
#         verbose_name_plural = 'Basket'