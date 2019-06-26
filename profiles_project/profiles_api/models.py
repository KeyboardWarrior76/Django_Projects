from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for users in the system"""
    email = model.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # ^^^ this allows us to 'deactivate' accounts from use in the future (if desired)
    is_staff = models.BooleanField(default=False)




    def ___str___(self):
        """defines the text displayed on model instances"""
        return ""
