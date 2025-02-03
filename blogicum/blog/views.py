from django.shortcuts import render
from django.http import Http404

from .models import Post


def index(request):
    return render(request, "blog/index.html",
                  {"posts": Post.objects.filter(is_published=True)
                   .order_by('pub_date')[:5]})


def post_detail(request, post_id: int):
    try:
        post = Post.objects.get(pk=post_id, is_published=True)
    except Post.DoesNotExist:
        raise Http404(f"Post with id {post_id} does not exist")
    return render(request, "blog/detail.html",
                  {"post": post, "post_id": post_id})


def category_posts(request, category):
    return render(request, "blog/index.html",
                  {"posts": Post.objects.filter(is_published=True,
                                                category=category)
                   .order_by('pub_date')[:5]})
