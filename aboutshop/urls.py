from django.urls import path
from . import views

app_name = 'aboutshop'  # Добавьте это для определения пространства имен

urlpatterns = [
    path('about/', views.about_view, name='about'),
]
