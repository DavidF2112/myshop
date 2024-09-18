from django.urls import path
from . import views

app_name = 'contact'  # This defines the namespace

urlpatterns = [
    path('contact/', views.contact_us, name='contact_us'),
]
