from django.shortcuts import render

# Create your views here.
from .models import Abonnement, Flux


def abonnement(request):
    context={'abonnement': Abonnement.objects.all()}
    return render(request, 'abonnement.html', context)

def flux(request):
    context={'flux': Flux.objects.all()}
    return render(request, 'flux.html', context)
