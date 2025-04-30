from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_("The Commeta ID / Username field must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)



class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        USER = 'user', _('User')

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
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

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
