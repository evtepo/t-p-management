DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": settings.db_name,
        "USER": settings.db_username,
        "PASSWORD": settings.db_password,
        "HOST": settings.db_host,
        "PORT": settings.db_port,
    }
}
