from .base import *

config_secret_prod = json.loads(open(CONFIG_SECRET_PROD_FILE).read())

# Database
DATABASES = config_secret_prod['django']['databases']

# Production Installed Apps
INSTALLED_APPS += [
    'storages'
]

# Allowed Hosts
ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com'
]

# AWS S3
# 1. IAM User Secret Info
AWS_ACCESS_KEY_ID = config_secret_prod['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config_secret_prod['aws']['AWS_SECRET_ACCESS_KEY']
# 2. Bucket Info
AWS_STORAGE_BUCKET_NAME = config_secret_prod['aws']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
S3_URL = f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# 3. Storage Folder Name - used in 'storage_backends.py'
AWS_STATIC_LOCATION = 'static'
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# 4. Access Domain
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# 5. Static/Media File Storage
## django-storages에 정의되어 있는 변수
STATICFILES_STORAGE = 'config.storage_backends.dj_storage_backend.S3StaticStorage'
DEFAULT_FILE_STORAGE = 'config.storage_backends.dj_storage_backend.S3PublicMediaStorage'
## custom한 storage - 직접 storage 인자에 넣어서 사용
## 예시)
##      upload = models.FileField(storage=PrivateMediaStorage())
PRIVATE_FILE_STORAGE = 'config.storage_backends.dj_storage_backend.S3PrivateMediaStorage'

# Debug
DEBUG = True
