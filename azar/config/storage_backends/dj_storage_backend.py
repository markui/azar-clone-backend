import os

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

django_settings = os.environ['DJANGO_SETTINGS_MODULE']


# S3 Staticfiles
class S3StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION


# S3 Public Mediafiles
class S3PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False


# S3 Private Mediafiles
class S3PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'private'
    custom_domain = False
