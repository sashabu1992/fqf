"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
   # ('en', _('English')),
    ('ru', _('Russian')),
]
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pn+6%0=)u66-5!z&z7b*&7wsskvg31nfe+&q%qq*!o4z5c!p-%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_HOST = 'DEV'
#DEV and PROD

if DEBUG_HOST == 'DEV':
    ALLOWED_HOSTS = ['127.0.0.1', 'django.kual.ru']
else:
    ALLOWED_HOSTS = ['localhost', 'fqf-nedvizhimost.ru', 'www.fqf-nedvizhimost.ru']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'websitesetting',
    'nedvizhimost',
    'crm',
    'uslugi',
    'django_ckeditor_5',
    'django.contrib.sitemaps',
    'users',
    'favorites',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_email_verification',
    'nedvizhimost.templatetags.filter'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
                'websitesetting.context_processors.website_settings',
            ],
        },
    },
]




WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG_HOST == 'DEV':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sashabgs_fqf',
            'USER': 'sashabgs_fqf',
            'PASSWORD': 'Jj&6urjg',
            'HOST': 'sashabgs.beget.tech',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'u0555309_django',
            'USER': 'u0555309_django',
            'PASSWORD': 'eY9fJ3dC7rjV9bO4',
            'HOST': 'localhost',
            'OPTIONS': {
                'read_default_file': '/var/www/u0555309/data/www/fqf-nedvizhimost.ru/my.cnf',
                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'glav'
LOGIN_URL = 'login'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
if DEBUG_HOST == 'DEV':
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = 'static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


THUMBNAIL_ALIASES = {
    '': {
        'preview': {'size': (360, 220), 'crop': "smart"},
        'baher': {'size': (1120, 371), 'crop': "smart"},
        'gal': {'size': (700, 400), 'crop': "smart"},
        'baherverh': {'size': (800, 216), 'crop': "smart"},
        'user': {'size': (400, 400), 'crop': "smart"},
        'officefoto': {'size': (400, 270), 'crop': "smart"},
    },
}


# функция, которая сделает пользователя активным
# после того, как он перейдет по ссылке
def verified_callback(user):
    user.is_active = True

EMAIL_VERIFIED_CALLBACK = verified_callback

# тема письма
EMAIL_MAIL_SUBJECT = 'Подтвердить email'
# шаблон письма в html
EMAIL_MAIL_HTML = 'registration/mail_body.html'
# текстовый шаблон
EMAIL_MAIL_PLAIN = 'registration/mail_body.txt'
# время жизни ссылки
EMAIL_MAIL_TOKEN_LIFE = 60 * 60
# шаблон, который увидят после перехода по ссылке
EMAIL_MAIL_PAGE_TEMPLATE = 'registration/confirm_template.html'
# домен для использования в ссылке
EMAIL_PAGE_DOMAIN = 'https://fqf-nedvizhimost.ru/'
EMAIL_MULTI_USER = True


EMAIL_HOST = 'mail.fqf-nedvizhimost.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@fqf-nedvizhimost.ru'
EMAIL_FROM_ADDRESS = 'info@fqf-nedvizhimost.ru'
EMAIL_HOST_PASSWORD = 'lI2kA9sO1yoQ9gC8'
EMAIL_USE_TLS = False

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
CKEDITOR_5_FILE_STORAGE = 'nedvizhimost.utils.CkeditorCustomStorage'
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}