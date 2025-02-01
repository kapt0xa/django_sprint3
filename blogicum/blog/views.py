from django.shortcuts import render
from django.http import Http404
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": """Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.""",
    },
]


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostStorage:
    def __init__(self, posts_val=None, default=False):
        if default:
            posts_val = posts
        self.posts = dict()
        if posts_val:
            for post in posts_val:
                self.posts[post["id"]] = post


post_storage = PostStorage(default=True)


def index(request):
    return render(request, "blog/index.html",
                  {"posts": reversed(post_storage.posts.items())})


def post_detail(request, post_id: int):
    if post_id not in post_storage.posts:
        raise Http404(f"post with id {id} does not exist")
    return render(request, "blog/detail.html",
                  {"post": post_storage.posts[post_id], "post_id": post_id})


def category_posts(request, category):
    filtred = []
    for id, post in post_storage.posts.items():
        if post["category"] == category:
            filtred.append((id, post))
    return render(
        request, "blog/category.html",
        {"posts": reversed(filtred), "category": category}
    )
