#CONFIGURACION BASE.py
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = '8ce%wc$91p%8mx)%rd=bgo68^5b9eny0qf^f5rbslbiz@*9h*2'

#TUPLA PARA INDICAR APPS INSTALADAS PROPIAS DE DJANGO
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

#TUPLA PARA INDICAR APPS INSTALADAS PROPIAS DE TERCEROS
THIRDPARTY_APPS = (
    'south',
)

#TUPLA PARA INDICAR APPS INSTALADAS PROPIAS DEL PROYECTO
LOCAL_APPS = (
    'apps.base',
)

# Application definition

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Speeducation.urls'

WSGI_APPLICATION = 'Speeducation.wsgi.application'

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

#######################################################################################################################

# CONFIGURACION LOCAL.py
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# CONFIGURACION PARA BASE DE DATOS LOCAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CAM',
        'USER' : 'admin',
        'PASSWORD' : 'pass',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
