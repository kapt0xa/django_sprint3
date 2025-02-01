from django.db import models
from django.contrib.auth.models import User

from core.models import PublishedModel 


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(PublishedModel):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(PublishedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.