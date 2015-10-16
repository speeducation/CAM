from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = '8ce%wc$91p%8mx)%rd=bgo68^5b9eny0qf^f5rbslbiz@*9h*2'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRDPARTY_APPS = (
    'south',
)

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
