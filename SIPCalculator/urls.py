from django.urls import path
from . import views

urlpatterns = [
    path('', views.sip_calculator, name='sip_calculator'),
    path('sip_calculator/', views.sip_calculator, name='sip_calculator'),  # Keep this line for the /sip_calculator/ URL
]
