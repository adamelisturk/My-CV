from django.shortcuts import render
from .models import GeneralSetting

def index(request):
    settings = GeneralSetting.objects.all()
    return render(request, 'core/index.html', {'settings': settings})

def contact(request):
    return render(request, 'core/contact.html')
