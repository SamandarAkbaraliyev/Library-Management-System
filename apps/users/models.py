from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        USER = 'user', _('User')

    id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    email = models.EmailField(
        _("Email"),
        unique=True,
    )
    role = models.CharField(
        max_length=10,
        verbose_name=_('Role'),
        choices=RoleChoices,
        default=RoleChoices.USER,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
