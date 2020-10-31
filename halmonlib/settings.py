"""
Django settings for halmonlib project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = 'f6pwq%)7+$^j7(iq35d!)tg%lxhs0lgc5t&g=r(_(qsz)-7e3e'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

ALLOWED_HOSTS = ['mlibrarypro.herokuapp.com']

# ALLOWED_HOSTS = ['halmonlibrary.com', 'localhost', '127.0.0.1', 'mlibrarypro.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'storages',
    'django.contrib.humanize',

    # third-party
    'crispy_forms',
    'django_extensions',
    'tinymce',
    'sorl.thumbnail',
    'social_django',

    # apps
    'account.apps.AccountConfig',
    'books.apps.BooksConfig',
    'donations.apps.DonationsConfig',
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_downloadview.SmartDownloadMiddleware',
]

ROOT_URLCONF = 'halmonlib.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'halmonlib.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2'
]

LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'halmonlib/static')
]

# Django_downloadview
# DOWNLOADVIEW_BACKEND = 'django_downloadview.nginx.XAccelRedirectMiddleware'

# Media Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Cloudinary Settings
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET')
}
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# DEFAULT_FILE_STORAGE = 'django_downloadview.storage.SignedStorage'

# Social Authentication Settings

# Github Oauth Settings
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET')

# Facebook Oauth Settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

# LinkedIn Oauth Settings
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')

# Crispy Settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Email Configurations
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 25
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_APP_HOST_PASSWORD = os.environ.get('EMAIL_APP_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Paypal Settings
PAYPAL_TEST = True

# Stripe Details
STRIPE_TEST_PUBLIC_KEY = os.environ.get('STRIPE_TEST_PUBLIC_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = os.environ.get('DJSTRIPE_WEBHOOK_SECRET')

# Tiny MCE Default Config
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 'auto', #1120
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak emoticons
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample | emoticons
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

django_heroku.settings(locals())
