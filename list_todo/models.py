from django.contrib.auth import get_user_model
from django.db import models

from .constants import SIZE_CUT_NAME

User = get_user_model()


class ListToDo(models.Model):
    name = models.CharField(
        verbose_name='Название задачи',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Добавьте краткое описание задачи'
    )
    add_date = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор задачи'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='Категория'
    )
    is_ready = models.BooleanField(
        verbose_name='Готова',
        help_text='Поставьте галочку, чтобы отметить '
                  'готовность задачи'
    )
    ready_date = models.DateTimeField(
        verbose_name='Сделать до: ',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Списки задач'
        verbose_name = 'список задач'
        ordering = ('-add_date',)

    def __str__(self):
        return self.name[:SIZE_CUT_NAME]


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL;'
                  ' разрешены символы латиницы, цифры,'
                  ' дефис и подчёркивание.'
    )

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'

    def __str__(self):
        return self.name[:SIZE_CUT_NAME]
