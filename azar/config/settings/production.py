from .base import *

config_secret_prod = json.loads(open(CONFIG_SECRET_PROD_FILE).read())

# Database
DATABASES = config_secret_prod['django']['databases']

# Production Installed Apps
INSTALLED_APPS += [
    'storages'
]

# AWS S3
# 1. IAM User Secret Info
AWS_ACCESS_KEY_ID = config_secret_prod['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret_prod['aws']['AWS_SECRET_ACCESS_KEY']
# 2. Bucket Info
AWS_STORAGE_BUCKET_NAME = config_secret_prod['aws']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
# 3. Storage Folder Name - used in 'storage_backends.py'
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'
STATICFILES_STORAGE = 'config.storage_backends.StaticStorage'

# Debug
DEBUG = True
