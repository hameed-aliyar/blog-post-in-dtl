from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts-home'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/new/', views.create, name='create-post'),
    path('post/<int:pk>/edit/', views.edit, name='edit'),
    path('post/<int:pk>/delete/', views.delete, name='delete-post'),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]