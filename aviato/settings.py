from pathlib import Path
import os
from dotenv import load_dotenv
# Load the .env file
load_dotenv()

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
    "social_django",
    'ckeditor',

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
    'social_django.middleware.SocialAuthExceptionMiddleware',
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
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
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
DEFAULT_FROM_EMAIL="Aviato group"


# Social Django Authentication

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_LINKEDIN_KEY = 'your-linkedin-client-id'
# SOCIAL_AUTH_LINKEDIN_SECRET = 'your-linkedin-client-secret'
SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')

# Production: https://yourdomain.com/auth/complete/github/

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000'
SOCIAL_AUTH_GITHUB_REDIRECT_URI = 'http://127.0.0.1:8000/auth/complete/github/'

SOCIAL_AUTH_GITHUB_SCOPE = ['user:email', 'read:user']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'account_module.social_pipeline.create_user',  # Ensure this is included
    # 'social_core.pipeline.user.create_user',  # Ensure this is included
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGIN_URL = 'login-page'
LOGOUT_URL = 'logout'

# Document
# todo:add thid field next time to send data with post method(default use get method to send username password(?))
# SOCIAL_AUTH_REQUIRE_POST = True


# ckeditor configuration
CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        'editor': 'ckeditor5',
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat']},
#             {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
#             {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar']},
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#         ],
#         'height': 300,
#         'width': '100%',
#     },
# }




