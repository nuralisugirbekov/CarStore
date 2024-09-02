from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Transport

# Create your views here.
def index(request):
    transports = Transport.objects.all()
    return render(request, 'shop/cars.html', {'transports': transports})


def single_transport(request, transport_id):
    transport=get_object_or_404(Transport, pk=transport_id)
    return render(request, 'shop/single_transport.html', {'transport': transport})