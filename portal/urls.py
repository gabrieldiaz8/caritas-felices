from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('campañas-activas', views.campañas_activas, name='Campañas Activas'),
    path('donaciones', views.donaciones, name='Donaciones'),
    path('contacto', views.contacto, name='Contacto'),
    path('sobre-nosotros', views.sobre_nosotros, name='Sobre Nosotros'),
    path('quiero-donar', views.quiero_donar, name='Quiero Donar'),
]
