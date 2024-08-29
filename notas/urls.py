from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='listar_notas'),
    path('crear/', views.crear_nota, name='crear_notas'),
]
