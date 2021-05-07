from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    slug = models.SlugField(verbose_name='Альтернативное название')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

# class Brand(models.Model):
#     name = models.CharField(max_length=200, verbose_name='Название бренда')
#     slug = models.SlugField(verbose_name='Алтернативное название')
#
#     class Meta:
#         verbose_name ='Брэнд'
#         verbose_name_plural ='Брэнд'
#
#     def __str__(self):
#         return self.name
