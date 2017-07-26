from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.

def index(request):
    random_tekst = "hallo ik ben Jef"
    return render(request, 'reservatie_open_cv/index.html', {'test': random_tekst})
