from django.db import models


class Blogs(models.Model):
    head = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Контент блога",
        help_text="Введите контент блога",
    )
    image = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите превью блога",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Признак публикации",
    )
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.head
