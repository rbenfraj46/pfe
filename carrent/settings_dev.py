from carrent.settings import *

DEBUG = True


if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_extensions',
        ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'carrental',
            'USER': 'myuser',
            'PASSWORD': '12345',
            'HOST': 'localhost',  
            'PORT': '5432',
        }
    } 
    



    INTERNAL_IPS = [
        '127.0.0.1',
        ]
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'tracking',
    #         'USER': 'tracking',
    #         'PASSWORD': 'tracking',
    #         'HOST': '127.0.0.1',
    #         'PORT': '5432',
    #     }
    # }
    TEMPLATE_DEBUG = DEBUG
    ALLOWED_HOSTS += ['*']
    RAVEN_CONFIG = { 'dsn': ''}
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
