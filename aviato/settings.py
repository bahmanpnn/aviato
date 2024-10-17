from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y%lf)nbd@6l9lfxfo!a@jm=10_o=cp!4wsm%w@ak)%zh^%qwrz'

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
    
    #local apps
    'home_module.apps.HomeModuleConfig',
    'contact_module.apps.ContactModuleConfig',
    'product_module.apps.ProductModuleConfig',
    'about_us_module.apps.AboutUsModuleConfig',
    'account_module.apps.AccountModuleConfig',
    'site_setting_module.apps.SiteSettingModuleConfig',
    'blog_module.apps.BlogModuleConfig',
    'order_module.apps.OrderModuleConfig',
    'user_profile_module.apps.UserProfileModuleConfig',
    'polls.apps.PollsConfig',
    'admin_panel_module.apps.AdminPanelModuleConfig',

    
    #third party apps
    'django_render_partial',
    'sorl.thumbnail',
    "crispy_forms",
    "crispy_bootstrap4",

]

# crispy forms config
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "uni_form"
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
# CRISPY_TEMPLATE_PACK = 'uni_form'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aviato.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'order_module.context_processors.basket_products',
            ],
        },
    },
]

WSGI_APPLICATION = 'aviato.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    BASE_DIR / 'static'
]

import os
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#media url is for load and server medias in site and templates
MEDIA_URL='/media/'

#media root is for uploading medias from user and site.it needs to add urls in base urls project
MEDIA_ROOT= BASE_DIR / 'medias'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='account_module.User'

# email config
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER="hamidbagheri042@gmail.com" #this is my test gmail please dont use it for yourself
EMAIL_HOST_PASSWORD='jqepansykjkurupk'
EMAIL_PORT=587
DEFAULT_FROM_EMAIL="Aviato group"

