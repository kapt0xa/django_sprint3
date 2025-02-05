from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_slug>/',
         views.category_posts, name='category_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
