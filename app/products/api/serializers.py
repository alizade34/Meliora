from rest_framework import serializers
from products.models import Product, Category, ProductImage
from django.contrib.auth import get_user_model

User = get_user_model()


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField(write_only=True)
    image_url = serializers.SerializerMethodField(read_only=True)

    def get_image_url(self, instance):
        return instance.image.url if instance.image else None

    class Meta:
        model = ProductImage
        fields = ('image', 'image_url')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')
    product_images = serializers.ListField(child=serializers.URLField(), write_only=True, required=False)

    def create(self, validated_data):
        images_data = validated_data.pop('product_images', [])
        product = Product.objects.create(**validated_data)

        for image_url in images_data:
            product_image = ProductImage.objects.create(image=image_url)
            product.images.add(product_image)

        return product

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "total_price": {"read_only": True},
            "images": {"read_only": True},
        }



    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['total_price'] = instance.price - (instance.discount_price or 0)
        repr_["wish_count"] = instance.wishlist.count()
        repr_['category'] = CategorySerializer(instance.category).data
        repr_['wishlist'] = WishlistSerializer(instance.wishlist.all(), many=True).data
        return repr_




class ProductCreateSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')
    product_images = serializers.ListField(child=serializers.URLField(), write_only=True, required=False)
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['category'] = CategorySerializer(instance.category).data
        repr_['user'] = instance.user.email
        return repr_

    def validate(self, attrs):
        price = attrs.get('price', None)
        if price < 0:
            raise serializers.ValidationError({"error": "Price must be positive number."})

        return super().validate(attrs)

    def create(self, validated_data):
        images_data = validated_data.pop('product_images', [])
        product = Product.objects.create(**validated_data)

        for image_url in images_data:
            ProductImage.objects.create(product=product, image=image_url)

        return product
