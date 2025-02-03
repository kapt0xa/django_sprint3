from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone

from .models import Post, Category


def index(request):
    return render(request, "blog/index.html",
                  {"post_list": Post.objects.filter(is_published=True, pub_date__lte=timezone.now()).order_by('pub_date')[:5]})
#pub_date__lte=timezone.now()


def post_detail(request, post_id: int):
    post = get_object_or_404(Post, pk=post_id, is_published=True, pub_date__lte=timezone.now())
    return render(request, "blog/detail.html",
                  {"post": post, "post_id": post_id})


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug, is_published=True)
    return render(request, "blog/index.html",
                  {"post_list": Post.objects
                   .filter(is_published=True,category=category, pub_date__lte=timezone.now())
                   .order_by('pub_date')[:5]})
