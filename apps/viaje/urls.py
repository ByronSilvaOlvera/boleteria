from django.urls import path

from . import views 

## nombre de la ruta 
app_name = 'viaje'
urlpatterns = [
    path('cliente/', views.ClienteListView.as_view() ),
    path('transporte/', views.TransporteListView.as_view() ),

    path('ruta/', views.RutaListView.as_view() , name="ruta-init"),
    path('ruta/add', views.RutaCreateView.as_view(), name="ruta-add" ),
    path('ruta/adds', views.RutaCreateViews.as_view(), name="ruta-adds" ),
    path('ruta/edit/<int:id>/', views.RutaListView.as_view(), name="ruta-detail" ),
   
]