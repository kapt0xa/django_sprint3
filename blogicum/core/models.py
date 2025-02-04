from django.db import models


class PublishedModel(models.Model):
    """Abstract model. Adds flag is_published and created_at."""

    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       help_text='Снимите галочку, '
                                       'чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True
