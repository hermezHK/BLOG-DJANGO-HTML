from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('crear/', views.crear_nota, name='crear_nota'),
    path('actualizar/<int:pk>/', views.actualizar_nota, name='actualizar_nota'),
    path('borrar/<int:pk>/', views.borrar_nota, name='borrar_nota'),
]
