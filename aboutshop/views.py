from django.shortcuts import render
from .models import Aboutshop

def about_view(request):
    aboutshop = Aboutshop.objects.first()
    
    context = {
        'name': aboutshop.name,
        'aboutshop': aboutshop
    }
    
    return render(request, 'shop/about.html', context)
