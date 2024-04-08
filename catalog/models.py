from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}. {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True, **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True, **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="Product")
    number_version = models.IntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=50, verbose_name='Название')
    is_current = models.BooleanField(default=True, verbose_name='Активная текущая')


    def __str__(self):
        return f'{self.number_version} ({self.name_version})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


