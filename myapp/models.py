from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    #user_type = models.CharField(max_length=20)  # Add any additional fields you need

    def _str_(self):
        return self.username