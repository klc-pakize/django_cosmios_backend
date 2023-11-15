from .base import *

THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": config("SQL_DATABASE"),
    "USER": config("SQL_USER"),
    "PASSWORD": config("SQL_PASSWORD"),
    "HOST": config("SQL_HOST"),
    "PORT": config("SQL_PORT"),
    "ATOMIC_REQUESTS": True,
    }
}
INTERNAL_IPS = [
    "127.0.0.1",
]