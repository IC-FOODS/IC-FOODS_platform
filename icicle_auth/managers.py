from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class ICICLEUserManager(BaseUserManager):
    """Custom User Manager to support our field changes"""

    def create_user(self, email, password, **extra_fields):
        """
        Create and save an UmiUser with the provided email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
