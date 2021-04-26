# myproject/settings/dev.py
from ._base import *
EMAIL_BACKEND = "django.core.mail.backend.console.EmailBackend"