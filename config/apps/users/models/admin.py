from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import User


class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True, verbose_name=_("Username"))
    image = models.ImageField(
        upload_to="admin_users/images/", blank=True, null=True, verbose_name=_("Image")
    )

    class Meta:
        verbose_name = _("Admin User")
        verbose_name_plural = _("Admin Users")

    def __str__(self):
        return f"{self.user.email}"

    def save(self, *args, **kwargs):
        if not self.user.is_staff:
            self.user.is_staff = True
            self.user.save(update_fields=["is_staff"])
        if not self.username:
            self.username = self.user.email.split("@")[0]
        super().save(*args, **kwargs)

    @property
    def is_active(self):
        return self.user.is_active
