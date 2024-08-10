from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(=8zleyu(u@8l^^%g)di1y6e3gkg-t7e8b=&ul9^!st$h*g+n9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2

STATIC_ROOT= BASE_DIR/'static'
MEDIA_ROOT= BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT ##django compressor
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED: ##django compressor
    COMPRESS_ENABLED = True
    COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
    COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"] ##django compressor

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

X_FRAME_OPTIONS = "SAMEORIGIN"