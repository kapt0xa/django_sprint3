from django.db import models


class PublishedModel(models.Model):
    """Abstract model. Adds flag is_published."""

    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       help_text='Снимите галочку, '
                                       'чтобы скрыть публикацию.')

    class Meta:
        abstract = True
