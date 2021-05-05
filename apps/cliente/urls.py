from django.urls import path

from apps.cliente.views import ClienteListView , ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView 



urlpatterns = [
    path('', ClienteListView.as_view()),
    path('add', ClienteCreateView.as_view(), name='cliente-add'),
    path('edit/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
]