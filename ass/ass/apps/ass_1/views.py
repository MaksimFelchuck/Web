from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def index(request):

    val = random.randrange(1, 1000)
    context = {
        'value': 'OMAEWA MOOO SHINDEIRU!!!',
        'val': str(val)
    }
    return render(request, 'index.html', context)
