from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q#n%^#-)iu!u9qzi3$e)og=zvxc4rh9p%-=l*oh3u1k&6&clkk'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend URL
    # "http://meguro.com.np",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    # "http://meguro.com.np",
]

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_COOKIE': 'access_token',
    'AUTH_COOKIE_REFRESH': 'refresh_token',

    'AUTH_COOKIE_SECURE': False,          # False for local dev (HTTP)
    'AUTH_COOKIE_SAMESITE': 'Lax',        # Lax recommended for local dev
    'AUTH_COOKIE_HTTP_ONLY': True,
    'AUTH_COOKIE_PATH': '/',

    'AUTH_COOKIE_REFRESH_SECURE': False,
    'AUTH_COOKIE_REFRESH_SAMESITE': 'Lax',
    'AUTH_COOKIE_REFRESH_HTTP_ONLY': True,
    'AUTH_COOKIE_REFRESH_PATH': '/',

}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'api.authentication.CookieJWTAuthentication',  # 👈 your custom class

    ),
}

ROOT_URLCONF = 'restaurant_backend.urls'

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

WSGI_APPLICATION = 'restaurant_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
