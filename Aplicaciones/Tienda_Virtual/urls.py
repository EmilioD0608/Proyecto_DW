from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('computadoras/', views.computadoras, name='computadoras'),
    path('laptops/', views.laptops, name='laptops'),
    path('teclados/', views.teclados, name='teclados'),
    path('mouse/', views.mouse, name='mouse'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('marcas/', views.marcas, name='marca'),
    path('perfil/', views.perfil, name='perfil'),

]