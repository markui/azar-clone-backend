from django.db import models

# Create your models here.
from config.storage_backends.custom_storage_backend import PrivateMediaStorage


class Document(models.Model):
    image = models.ImageField(storage=PrivateMediaStorage())
