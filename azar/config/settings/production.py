from .base import *

config_secret_prod = json.loads(open(CONFIG_SECRET_PROD_FILE).read())

# Database
DATABASES = config_secret_prod['django']['databases']

# Local Installed Apps
INSTALLED_APPS += [

]

# Debug
DEBUG = False
