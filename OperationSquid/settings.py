"""
Django settings for OperationSquid project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.contrib.messages import constants as messages


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$f(t#78+b72!kxbj4=wjh637+ymcg!gb((z%)9&6^e-fg8a9b-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'social.apps.django_app.default',
    'user_account',
    'events',
    'sharing',
    'reservations',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'OperationSquid.preprocessors.get_active_events',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'OperationSquid.urls'

WSGI_APPLICATION = 'OperationSquid.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pts2',
        'USER': 'pts2',
        'PASSWORD': 'uXsPQQzmsuCATavF',
        'HOST': 'terarion.com',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


LOGIN_REDIRECT_URL = "/user/login/"
LOGIN_URL = "/user/login/"
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "statics/media")
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics/static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "statics/templates"),
)

# Crispy Forms Setup

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Messages tags

MESSAGE_TAGS = {
    messages.DEBUG: 'default',
    messages.INFO: 'primary',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Social Auth
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/user/login/"
SOCIAL_AUTH_LOGIN_URL = "/user/login/"

SOCIAL_AUTH_DEFAULT_USERNAME = "Jaden Doe"

SOCIAL_AUTH_TWITTER_KEY = "cOjawfhibufn6jJh6GSQSZk69"
SOCIAL_AUTH_TWITTER_SECRET = "ML2pD3CTNnBnAcjubqmXFmK8kuRHmLWSfy9M81joC9xz2EFdu2"

SOCIAL_AUTH_FACEBOOK_KEY = "681442585301110"
SOCIAL_AUTH_FACEBOOK_SECRET = "0618b289a90a490018803451a4ffcc74"
