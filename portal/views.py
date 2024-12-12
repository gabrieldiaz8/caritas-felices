from django.shortcuts import render
from .models import Campaign

def inicio(request):
    return render(request, 'sections/index.html')

def campañas_activas(request):
    activas = Campaign.obtener_activas()
    return render(request, 'sections/events.html', {'campañas_activas': activas})

def donaciones(request):
    return render(request, 'sections/causes.html')
    
def contacto(request):
    return render(request, 'sections/contact.html')

def sobre_nosotros(request):
    return render(request, 'sections/about.html')

def quiero_donar(request):
    return render(request, 'sections/donation.html')