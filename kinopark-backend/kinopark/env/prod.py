from kinopark.base import *
from kinopark.conf import POSTGRESQL_URL

import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["localhost:8000","localhost","localhost:5173","155.228.90.158"]

DATABASES = {
    "default": dj_database_url.config(default=POSTGRESQL_URL),
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:5173",
    "http://165.227.173.159",
]
CORS_ALLOW_CREDENTIALS = True