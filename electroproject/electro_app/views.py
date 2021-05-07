from django.shortcuts import render
from .models import *

def base_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)
