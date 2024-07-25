BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.secret_key

DEBUG = settings.debug

ALLOWED_HOSTS = settings.allowed_hosts.split(",")

ROOT_URLCONF = "management.urls"

WSGI_APPLICATION = "management.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    "127.0.0.1",
]

# SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = settings.session_cookie_time * 24 * 60 * 60

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/home/"
LOGOUT_REDIRECT_URL = "/home/"
