from .models import Post, PostImage
from django.contrib import admin

class PostImageInline(admin.TabularInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
    ]
    list_display = ['title', 'author', ]
    search_fields = ['title', ]
    list_filter = ['author', ]