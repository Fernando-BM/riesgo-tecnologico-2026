from django.urls import path
from . import views

app_name = 'agencia'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    #Url's parametrizadas <TIPO:NOMBRE_VAR>
    #servicios principales menú superior
    path('<str:servicio>/', views.seccion, name='seccion'),
    #servicios secundarios del menú superior
    path('<str:servicio>/<str:subtema>/', views.detalle, name='detalle'),
]