
from django.db import models
from services.mixins import DateMixin
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(DateMixin):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

