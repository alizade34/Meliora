from rest_framework import serializers
from blogs.models import Post, PostImage

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField(write_only=True)
    image_url = serializers.SerializerMethodField(read_only=True)

    def get_image_url(self, instance):
        return instance.image.url if instance.image else None

    class Meta:
        model = PostImage
        fields = ('image', 'image_url')
class PostListSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True, source='postimage_set')
    post_images = serializers.ListField(child=serializers.URLField(), write_only=True, required=False)

    def create(self, validated_data):
        images_data = validated_data.pop('post_images', [])
        post = Post.objects.create(**validated_data)

        for image_url in images_data:
            post_image = PostImage.objects.create(image=image_url)
            post.images.add(post_image)

        return post

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "images": {"read_only": True},
        }