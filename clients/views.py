from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import generics
from .models import Client, HealthProgram
from .serializers import ClientSerializer, HealthProgramSerializer
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Non-API Views
def home(request):
    """Display the homepage."""
    return render(request, 'clients/home.html')

def program_create(request):
    """Display the program creation page."""
    return render(request, 'clients/program_create.html')

def client_create(request):
    """Display the client registration page."""
    return render(request, 'clients/client_create.html')

def client_search(request):
    """Search for clients by name or email."""
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(email__icontains=query)
        )
    return render(request, 'clients/client_search.html', {
        'clients': clients,
        'query': query
    })

class ClientDetailView(DetailView):
    """Display a client's profile."""
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

# API Views
@csrf_exempt
class HealthProgramListCreateAPIView(generics.ListCreateAPIView):
    """List all health programs or create a new one."""
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

@csrf_exempt
class HealthProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a health program by ID."""
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

@csrf_exempt
class ClientListCreateAPIView(generics.ListCreateAPIView):
    """List all clients or create a new one."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@csrf_exempt
class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a client by ID."""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer