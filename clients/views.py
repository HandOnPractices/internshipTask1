from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView
from .models import Client, HealthProgram, CustomUser
from django.db.models import Q
from .serializers import ClientSerializer, HealthProgramSerializer
from rest_framework import generics
from django.contrib.auth import login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(request):
    """View to render the home page."""
    return render(request, 'clients/home.html')


# Admin registration view
def register(request):
    """Handle admin (doctor) registration."""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        unique_key = request.POST.get('unique_key')

        if unique_key != settings.ADMIN_REGISTRATION_KEY:
            messages.error(request, 'Invalid unique key.')
            return render(request, 'clients/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'clients/register.html')

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role='admin'
        )
        login(request, user)
        messages.success(request, 'Registration successful! You are now logged in.')
        return redirect('home')

    return render(request, 'clients/register.html')

# Admin login/logout views
def login_view(request):
    """Handle admin login."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.role == 'admin':
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password, or not an admin.')
            return render(request, 'clients/login.html')
    return render(request, 'clients/login.html')

def logout_view(request):
    """Handle admin logout."""
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

# Client views
@login_required
def client_create(request):
    """Display the client registration page."""
    return render(request, 'clients/client_create.html')


@login_required
def client_search(request):
    """View to search for clients by name or email"""
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | 
            Q(email__icontains=query)
        )
    return render(request, 'clients/client_search.html', {
        'clients': clients,
        'query': query
    })


@login_required
def program_create(request):
    """Display the program creation page."""
    return render(request, 'clients/program_create.html')

@login_required
class ClientDetailView(DetailView):
    """View to display a client's profile."""
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'


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