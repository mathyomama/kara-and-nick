"""
Django settings for wedding project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__) # This will be a relative path and depends on where it was invoked from
DJANGO_DIR = os.path.join(SETTINGS_DIR, os.pardir)
DJANGO_DIR = os.path.abspath(DJANGO_DIR) # This should ultimately be /home/pi/webapps/wedding/wedding
WEB_DIR = os.path.dirname(DJANGO_DIR) # This should be /home/pi/webapps/wedding/

# Where django looks for templates
TEMPLATE_DIRS = (
		os.path.join(DJANGO_DIR, 'templates'),
		)

# Where django looks for static files
STATICFILES_DIRS = (
		os.path.join(DJANGO_DIR, 'static'),
		)
# Where django will collect static files for deployment, should be "/home/pi/webapps/wedding/static/"
STATIC_ROOT = os.path.join(WEB_DIR, 'static')

# Where django will store user uploaded files, should be "/home/pi/webapps/wedding/media/"
MEDIA_ROOT = os.path.join(WEB_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '85nc(ftxb358c^ds2x&nzl!(&8b486o1sf5y4lb=p863g)oqvg'

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
	'localflavor',
	'accommodations',
	'contacts',
	'gallery',
	'guestbook',
	'our_story',
	'registry',
	'rsvp',
	'the_big_day',
	'things_to_do',
	'wedding_party',
	'welcome',
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

ROOT_URLCONF = 'wedding.urls'

WSGI_APPLICATION = 'wedding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'weddingdb',
			'USER': 'pi',
			'PASSWORD': 'password',
			'HOST': 'localhost',
			'PORT': '',
			}
		}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
