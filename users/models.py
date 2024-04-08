from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Старна', **NULLABLE)
    token = models.CharField(max_length=10, verbose_name='Верификация', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
