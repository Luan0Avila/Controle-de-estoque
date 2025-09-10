from django.urls import path
from . import views

app_name = 'estoque_insumo'

urlpatterns = [
    path('', views.estoque_insumo_view, name='home'),
    path('estoque/novo_material', views.cadastrar_novo_material, name='cadastrar_material'),
]
