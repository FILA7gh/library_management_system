from pathlib import Path

from celery.schedules import crontab

from core.settings import load_env

from core.settings.jwt import *

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = load_env.SECRET_KEY

DEBUG = load_env.DEBUG

ALLOWED_HOSTS = load_env.ALLOWED_HOSTS


INSTALLED_APPS = [
    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party applications
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",

    # Project applications
    "apps.authors.apps.AuthorsConfig",
    "apps.books.apps.BooksConfig",
    "apps.users.apps.UsersConfig",
    "apps.favorites.apps.FavoritesConfig",
]

MIDDLEWARE = [
    "querycount.middleware.QueryCountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": load_env.POSTGRES_DB,
        "USER": load_env.POSTGRES_USER,
        "PASSWORD": load_env.POSTGRES_PASSWORD,
        "HOST": load_env.POSTGRES_HOST,
        "PORT": load_env.POSTGRES_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

CELERY_BROKER_URL = "redis://localhost:6379/0"

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

CELERY_BEAT_SCHEDULE = {
    "send-new-books-notification-every-minute": {
        "task": "apps.books.tasks.send_new_books_notification",
        "schedule": crontab(minute="*"),
    },
    "send-anniversary-books-notification-every-minute": {
        "task": "apps.books.tasks.send_anniversary_books_notification",
        "schedule": crontab(minute="*"),
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.akmatbekovvv@gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "akmatbekovvv@gmail.com"
EMAIL_HOST_PASSWORD = load_env.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = "akmatbekovvv@gmail.com"


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"
