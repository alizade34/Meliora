
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(DateMixin):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    author = models.CharField(blank=True, null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=Uploader.upload_image_of_blog, blank=True, null=True)

    def __str__(self):
        return self.title


