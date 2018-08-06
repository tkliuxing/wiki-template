"""
Django settings for testsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r^b*m=1-89abwmd)u*tp7ypx#k(3mxs_d(pm-&6=sk(2^yay^^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.humanize.apps.HumanizeConfig',
    'django.contrib.auth.apps.AuthConfig',
    'django.contrib.contenttypes.apps.ContentTypesConfig',
    'django.contrib.sessions.apps.SessionsConfig',
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.messages.apps.MessagesConfig',
    'django.contrib.staticfiles.apps.StaticFilesConfig',
    'django.contrib.admin.apps.AdminConfig',
    'django.contrib.admindocs.apps.AdminDocsConfig',
    'sekizai',
    'sorl.thumbnail',
    "django_nyt.apps.DjangoNytConfig",
    "wiki.apps.WikiConfig",
    "wiki.plugins.macros.apps.MacrosConfig",
    'wiki.plugins.help.apps.HelpConfig',
    'wiki.plugins.links.apps.LinksConfig',
    "wiki.plugins.images.apps.ImagesConfig",
    "wiki.plugins.attachments.apps.AttachmentsConfig",
    "wiki.plugins.notifications.apps.NotificationsConfig",
    'wiki.plugins.globalhistory.apps.GlobalHistoryConfig',
    'wiki.plugins.redlinks.apps.RedlinksConfig',
    'wiki_template.apps.WikiTemplateConfig',
    'mptt',
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'testsite.urls'

WSGI_APPLICATION = 'testsite.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG,
        },
    },
]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGIN_REDIRECT_URL = reverse_lazy('wiki:get', kwargs={'path': ''})

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

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i:s"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'testsite/static'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

WIKI_MARKDOWN_HTML_WHITELIST = [
    'center', 'style', 'div'
]

WIKI_MARKDOWN_HTML_ATTRIBUTES = {
    '*': ['style']
}

WIKI_MARKDOWN_HTML_STYLES = [
    'padding', 'width', 'color', 'float', 'clear', 'background'
]

WIKI_ANONYMOUS = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = False
WIKI_ANONYMOUS_WRITE = False
WIKI_ANONYMOUS_CREATE = False
