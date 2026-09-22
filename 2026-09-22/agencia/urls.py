from django.urls import path
from . import views

app_name = 'agencia'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<str:servicio>/', views.seccion, name='seccion'),
    path('<str:servicio>/<str:subtema>/', views.detalle, name='detalle'),
]