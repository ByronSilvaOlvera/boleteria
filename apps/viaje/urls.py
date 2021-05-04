from django.urls import path

from . import views 


urlpatterns = [
    path('cliente/', views.ClienteListView.as_view() ),
    path('transporte/', views.TransporteListView.as_view() ),

    path('ruta/', views.RutaListView.as_view() ),
    path('ruta/add', views.RutaCreateView.as_view(), name="ruta-add" ),
   
]