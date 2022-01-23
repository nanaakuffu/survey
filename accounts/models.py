from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'),
                              max_length=150,
                              unique=True
                              )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'
