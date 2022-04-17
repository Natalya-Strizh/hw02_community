# posts/urls.py
from django.urls import path
from django.urls import include
from . import views
app_name = 'posts'

urlpatterns = [
    path('',  views.index, name = 'index'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_list'),
] 