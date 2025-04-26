from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=15, blank=False)
    email = models.EmailField(unique=True)
    sex = models.TextField(blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


