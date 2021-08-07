from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class UserType(models.TextChoices):
        ADMIN = 'admin'
        SPECIALIST = 'specialist'
        PERSON = 'person'

    role = models.CharField(max_length=20, choices=UserType.choices, default=UserType.PERSON)

