from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

import dj_database_url
import environ
import cloudinary.uploader
import cloudinary.api
import cloudinary


env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["themirrored-production.up.railway.app", "www.themirrored.com", "themirrored.com"]

cloudinary.config( 
  cloud_name = env('CLOUD_NAME'), 
  api_key = env("CLOUD_API_KEY"), 
  api_secret = env("CLOUD_API_SECRET") 
)

DATABASES = {
    "default": dj_database_url.config(default=env('postgresql://postgres:AD*23eCG54dEe43aCe**4a2ec4*C*ef4@monorail.proxy.rlwy.net:44724/railway'), conn_max_age=1800),
}

EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
# EMAIL_HOST_USER = 'clarksvillesdlbc@gmail.com'
# EMAIL_HOST_PASSWORD = '4DC6317573C5B115FB1FFE24C96AF91CBA4A'
# DEFAULT_FROM_EMAIL = 'clarksvillesdlbc@gmail.com'
EMAIL_HOST_USER = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')