from django.db import models
from django.contrib.auth.models import User

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Иднетификатор', unique=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField('Название места', max_length=256)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации', blank=False)
    author = models.ForeignKey(User, verbose_name='Автор публикации',
                               on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='Местоположение',
                                 on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return self.title

# Create your models here.
