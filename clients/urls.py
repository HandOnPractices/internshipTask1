from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.client_search, name='client_search'),
    path('program/create/', views.program_create, name='program_create'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    # API URLs
    path('api/programs/', views.HealthProgramListCreateAPIView.as_view(), name='program_list_create_api'),
    path('api/programs/<int:pk>/', views.HealthProgramRetrieveUpdateDestroyAPIView.as_view(), name='program_detail_api'),
    path('api/clients/', views.ClientListCreateAPIView.as_view(), name='client_list_create_api'),
    path('api/clients/<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_detail_api'),
]
