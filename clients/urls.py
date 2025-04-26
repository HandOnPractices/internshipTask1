from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.client_search, name='client_search'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('api/client/<int:pk>/', views.ClientDetailAPIView.as_view(), name='client_detail_api'),

]