from django.urls import path
from . import views

app_name = 'estoque_insumo'

urlpatterns = [
    path('register/', vews.register_user, name='register' )
]