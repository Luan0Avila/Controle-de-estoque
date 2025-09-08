from django.urls import path
from . import views

urlpatterns = [
    path('', views.estoque_insumo_view, name='estoque_insumo'),
]
