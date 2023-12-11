# users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, bypass_password_validation=False, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:
            if not bypass_password_validation:
                try:
                    validate_password(password, user)
                except ValidationError as e:
                    raise ValidationError({'password': e.messages})
            user.set_password(password)
        else:
            raise ValueError(_('The Password must be set'))

        user.is_active = extra_fields.get('is_active', True)
        user.is_staff = extra_fields.get('is_staff', False)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('user_type') != 'admin':
            raise ValueError('Superuser must have user_type=admin.')

        return self.create_user(email, password, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    )

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=150,
                            unique=False, blank=True, null=True)
    role = models.CharField(_('role'), max_length=150,
                            unique=False, blank=True, null=True)
    registration = models.CharField(
        _('registration'), max_length=150, unique=False, blank=True, null=True)
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default='guest')
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
