from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import Client, HealthProgram
from django.db.models import Q
from .serializers import ClientSerializer, HealthProgramSerializer
from rest_framework import generics


def home(request):
    """View to render the home page."""
    return render(request, 'clients/home.html')


def client_search(request):
    """View to search for clients by name."""
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    return render(request, 'clients/client_search.html', {
        'clients': clients,
        'query': query
    })

class ClientDetailView(DetailView):
    """View to display a client's profile."""
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

class ClientDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a client's profile.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'


# API views for Client
class ClientListCreateAPIView(generics.ListCreateAPIView):
    """List all clients or create a new one."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a client by ID."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# API Views for HealthProgram
class HealthProgramListCreateAPIView(generics.ListCreateAPIView):
    """List all health programs or create a new one."""
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

class HealthProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a health program by ID."""
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer