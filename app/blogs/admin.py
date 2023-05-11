from .models import Post
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author',]
    search_fields = ['title',]
    list_filter = ['author', ]

