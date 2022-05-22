import environ

from docmanager.settings.base import *

env = environ.Env()

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

CORS_ALLOWED_ORIGINS = [
    "https://solidjs-docmanager.vercel.app",
    "http://localhost:3000",
]

DATABASES = {"default": env.db()}
