import os
import sys
from pathlib import Path
from environs import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 1

ALLOWED_HOSTS = env.str("DJANGO_ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = ['https://nesssery.mystore.fun']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',

    'stores.apps.StoresConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG == True:
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env.str("DB_USER"),
            'PASSWORD': env.str("DB_PASSWORD"),
            'HOST': env.str("DB_HOST"),
            'PORT': env.str("DB_PORT"),
            'NAME': env.str("DB_NAME")
        }
    }
   
else:
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env.str("DB_USER"),
            'PASSWORD': env.str("DB_PASSWORD"),
            'HOST': env.str("DB_HOST"),
            'PORT': env.str("DB_PORT"),
            'NAME': env.str("DB_NAME")
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'
else:
    STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomUserCreationForm',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'home-view'
ACCOUNT_LOGOUT_REDIRECT = 'home-view'

SITE_ID = 1

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'users.backends.CaseInsensitiveModelBackend'
)

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True


DEFAULT_FROM_EMAIL = 'nesssery.tech@gmail.com'
EMAIL_HOST_USER = 'nesssery.tech@gmail.com'
EMAIL_HOST_PASSWORD = 'athbojhxxumcpuka'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
if DEBUG == False:
    RECIPIENT_ADDRESS_ADMIN = ['nesssery.tech@gmail.com']
    RECIPIENT_ADDRESS = ['nesssery.tech@gmail.com']
else:
    RECIPIENT_ADDRESS_ADMIN = ['nesssery.tech@gmail.com',]
    RECIPIENT_ADDRESS = ['nesssery.tech@gmail.com',]


CRISPY_TEMPLATE_PACK = 'bootstrap4'

CRON_PYTHON_INTERPRETEUR = sys.executable
CRON_DJANGO_MANAGE_PY = os.path.join(BASE_DIR, 'manage.py')
CRON_DJANGO_HOME = os.path.join(BASE_DIR, '/')
CRON_LOG_DIR = os.path.join(BASE_DIR, 'logs/')
CRONTAB_DJANGO_PROJECT_NAME = "coding-challenge"
CRONJOBS = [
    ('*/1 * * * *', 'utils.checkUserViews.handle', '>> {}'.format(os.path.join(BASE_DIR, 'logs/checkUserViews.log'))),
    ('*/1 * * * *', 'utils.test.hello', '>> {}'.format(os.path.join(BASE_DIR, 'logs/test.log'))),]


