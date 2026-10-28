import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "change-this-development-key")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "*"]
INSTALLED_APPS = ["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","rest_framework","rest_framework.authtoken","restaurant"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF = "littlelemon.urls"
TEMPLATES = [{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.debug","django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "littlelemon.wsgi.application"
if os.environ.get("DB_ENGINE","mysql").lower() == "sqlite":
    DATABASES = {"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
else:
    DATABASES = {"default":{"ENGINE":"django.db.backends.mysql","NAME":os.environ.get("MYSQL_DATABASE","littlelemon"),"USER":os.environ.get("MYSQL_USER","root"),"PASSWORD":os.environ.get("MYSQL_PASSWORD",""),"HOST":os.environ.get("MYSQL_HOST","127.0.0.1"),"PORT":os.environ.get("MYSQL_PORT","3306"),"OPTIONS":{"charset":"utf8mb4"}}}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {"DEFAULT_AUTHENTICATION_CLASSES":["rest_framework.authentication.TokenAuthentication","rest_framework.authentication.SessionAuthentication","rest_framework.authentication.BasicAuthentication"],"DEFAULT_PERMISSION_CLASSES":["rest_framework.permissions.IsAuthenticatedOrReadOnly"],"DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination","PAGE_SIZE":10}
