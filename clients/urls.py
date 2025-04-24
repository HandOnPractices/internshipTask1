from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.client_search, name='client_search'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
]