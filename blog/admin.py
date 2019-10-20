from django.contrib import admin
from django.urls import path
from . import views
from .models import Post

admin.site.register(Post)
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
