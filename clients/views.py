from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import Client
from django.db.models import Q

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