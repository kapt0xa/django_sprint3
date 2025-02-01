from django.shortcuts import render
from django.http import Http404


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
