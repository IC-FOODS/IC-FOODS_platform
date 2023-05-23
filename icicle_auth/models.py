import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from icicle_base.models import UUIDBaseModel
from icicle_auth.managers import ICICLEUserManager

class ICICLEUser(AbstractUser, UUIDBaseModel):
    """
    Custom User model for ICICLE
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    email_is_verified = models.BooleanField(default=False)

    organization = models.CharField(max_length=64, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ICICLEUserManager()
