import re
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def soba(request, naziv_sobe):
    return render(request, 'chat/soba.html', {
        'naziv_sobe': naziv_sobe
    })