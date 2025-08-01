from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_name = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите свой аватар",)
    phone = models.CharField(max_length=35, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=50, verbose_name="Страна", blank=True, null=True, help_text="Укажите страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
