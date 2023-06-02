from django.db import models
from ckeditor.fields import RichTextField
from services.uploader import Uploader



class GeneralSettings(models.Model):
    logo = models.ImageField(upload_to=Uploader.upload_image_of_logo)
    email = models.EmailField(blank=True, null=True)
    instagram = models.CharField(blank=True, null=True, max_length=255)
    facebook = models.CharField(blank=True, null=True, max_length=255)
    twitter = models.CharField(blank=True, null=True, max_length=255)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    location = RichTextField(blank=True, null=True)
    footer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.instagram