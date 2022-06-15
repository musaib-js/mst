from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name='blogHome'),
    path('policy', views.policy, name='policy'),
    path('privacy', views.privacy, name='privacy'),
    path('<str:slug>/', views.blogPost, name='blogPost'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)