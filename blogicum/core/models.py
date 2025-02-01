from django.db import models


class PublishedModel(models.Model):
    """Abstract model. Adds flag is_published."""

    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True
