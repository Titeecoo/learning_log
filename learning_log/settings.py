"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qgp+v7q8o8*j#ha284+rrk48t*xl+pngclx^g*4*mb(_68lbt#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'bootstrap3',

    # My apps
    'learning_logs',
    'users',
]

# The installed_apps list is just a tuple that tells Django which apps work 
# together to make up the project.

# When we add our own app to installed_apps, we have to tell Django to modify
# the database so it can store its information. From the terminal with an open
# virtual environment, you type:
# python3 manage.py makemigrations app_name (learning_logs in this case)

# makemigrations tells Django to figure out how to modify the database so it
# can store data associated with any new models we've defined

# To apply the migration, we type:
# python3 manage.py migrate

# Whenever we want to modify the data that Learning Log (the project) manages,
# we'll follow these 3 steps: modify models.py, call makemigrations on
# learning_logs (the app), and tell Django to migrate the project.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# My settings
LOGIN_URL ='/users/login/'

# Settigns for django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
}

# Heroku settings
cwd = os.getcwd()
if cwd == '/app' or cwd[:4] == '/tmp':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }

    # Honor the 'X-Forwarded-Proto' header for request.is_secure().
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers.
    ALLOWED_HOSTS = ['*', '0.0.0.0']

    # Static asset configuration
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

# This is alot to deal with, so let's break it down. The function getcwd() gets
# the current working directory the file is running from. In a Heroku
# deployment, the directory is always /app. In a local deployment, the
# directory is usually the name of the project folder (learning_log in this
# case). The if test ensures that the settings in this block apply only when
# the project is deployed on Heroku. This structure allows us to have one
# settings file that works for our local development environment as well as
# the live server.
# We import dj_database_url to help configure the database on Heroku. Heroku
# uses PostgreSQL (also called Postgres), a more advanced database than SQLite,
# and these settings configure the project to use Postgres on Heroku. The
# rest of the settings support HTTPS requests, ensure that Django will serve
# the project from Heroku's URL, and set up the project to serve static files
# correctly on Heroku.

# We also made a procfile that weirdly has no file extension (I can't tell what
# type of file it is). A Procfile tells Heroku which processes to start in
# order to serve the project properly. This is a one-line file that we saved
# as Procfile. The line in Procfile tells Heroku to use gunicorn as a server
# and to use the settings in learning_log/wsgi.py to launch the app. The 
# log-file flag tells Heroku the kinds of events to log.