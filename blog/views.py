from django.shortcuts import render

from .models import Post, Category
from .constants import MAX_POSTS_ON_PAGE


def index(request):
    return render(request, 'blog/index.html',
                  {'post_list': Post
                   .filter_published()
                   .order_by('pub_date')[:MAX_POSTS_ON_PAGE]})


def post_detail(request, post_id: int):

    return render(request, 'blog/detail.html',
                  {'post': Post.get_by_id_or_404(post_id)})


def category_posts(request, category_slug):
    category = Category.get_by_slug_or_404(category_slug)

    return render(request, 'blog/index.html',
                  {'post_list': Post
                   .filter_published()
                   .filter(category=category)
                   .order_by('pub_date')})
