from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import Http404

from core.models import PublishedModel
from .constants import NAME_MAX_LEN, REPORT_NAME_MAX_LEN


class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=NAME_MAX_LEN)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True,
                            help_text='Идентификатор страницы для URL;'
                            ' разрешены символы латиницы, '
                            'цифры, дефис и подчёркивание.')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    @staticmethod
    def filter_published():
        """Returns filters published categories."""
        return Category.objects.filter(
            is_published=True)

    @staticmethod
    def get_by_slug_or_404(id):
        """Returns published category or raises 404."""
        try:
            return Category.filter_published().get(slug=id)
        except Category.DoesNotExist:
            raise Http404(f'Category with id {id} not found.')

    def __str__(self):
        if len(self.title) > REPORT_NAME_MAX_LEN:
            return self.title[:REPORT_NAME_MAX_LEN] + '…'
        return self.title


class Location(PublishedModel):
    name = models.CharField('Название места', max_length=NAME_MAX_LEN)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=NAME_MAX_LEN)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации', blank=False,
                                    help_text='Если установить дату'
                                    ' и время в будущем —'
                                    ' можно делать отложенные публикации.')
    author = models.ForeignKey(User, verbose_name='Автор публикации',
                               on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='Местоположение',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.SET_NULL, null=True)

    @staticmethod
    def filter_published():
        """Returns filters published posts, not in future."""
        return Post.objects.filter(is_published=True,
                                   pub_date__lte=timezone.now(),
                                   category__is_published=True)

    @staticmethod
    def get_by_id_or_404(id):
        """Returns published post or raises 404."""
        try:
            return Post.filter_published().get(pk=id)
        except Post.DoesNotExist:
            raise Http404(f'Post with id {id} not found.')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        if len(self.title) > REPORT_NAME_MAX_LEN:
            return self.title[:REPORT_NAME_MAX_LEN] + '…'
        return self.title

# Create your models here.
