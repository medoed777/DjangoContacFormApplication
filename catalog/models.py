from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        null=True, verbose_name="Цена", help_text="Введите цену продукта"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Введите название страны")
    inn = models.CharField(max_length=15, verbose_name="ИНН", help_text="Введите инн организации", blank=True, null=True,)
    address = models.TextField(verbose_name="Адрес", help_text="Введите адрес организации", blank=True, null=True,)
    email = models.EmailField(blank=True, null=True,)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["country"]

    def __str__(self):
        return self.country