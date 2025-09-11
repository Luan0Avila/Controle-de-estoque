from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('register/create/', views.register_create, name='register_create'),]