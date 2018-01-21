from .base import *

config_secret_local = json.loads(open(CONFIG_SECRET_LOCAL_FILE).read())

# Database
DATABASES = config_secret_local['django']['databases']

# Local Installed Apps
INSTALLED_APPS += [
    'django_extensions'
]

# Debug
DEBUG = True
