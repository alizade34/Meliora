from .models import Post, PostImage
from django.contrib import admin

class PostImageInline(admin.TabularInline):
    model = PostImage

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PostImage,
    ]
    list_display = ['title', 'author', ]
    search_fields = ['title', ]
    list_filter = ['author', ]