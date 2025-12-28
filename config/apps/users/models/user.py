from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base_user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True, verbose_name=_("Email"))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active Account"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Admin Staff"))

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["-date_joined"]),
            models.Index(fields=["is_active", "-date_joined"]),
        ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
