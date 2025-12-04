from decouple import config

ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)

ENV_ID = config("KINOPARK_ENV_ID", default="local", cast=str)

POSTGRESQL_URL = config(
    "POSTGRESQL_URL",
    default="postgres://kino:12345@localhost:5432/kino",
    cast=str,
)

SECRET_KEY = 'django-insecure-8lgxny-%nzy9^#r%2p-3na$#*$y4q8(w1xru#an=nf#gbo4f03'