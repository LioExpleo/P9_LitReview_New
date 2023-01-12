from django.shortcuts import render

# Create your views here.
from .models import Abonnement, Ticket, Review, Review2

# importer la classe du formulaire
from .formulaire import ReviewForm, TicketForm, AbonnementForm, Review2Form

# Pour créer le formulaire, faire l'instanciation sur la classe du formulaire importé ReviewForm
# indiquer le formulaire sous forme d'un dictionnaire avec {]


# On définit alors notre classe qui va permettre de générer notre formulaire en la faisant dériver de ModelForm et en lui spécifiant le modèle à inclure Contact

def indexReview(request):
     form = ReviewForm(request.POST or None)
     messages = "enregistrement ok"
     if form.is_valid():
        form.save()
        form = ReviewForm()
     return render(request, 'indexReview.html', {'form': form, 'message': messages} )

def indexReview2(request):
     form = Review2Form(request.POST or None)
     messages = "enregistrement ok"
     if form.is_valid():
        form.save()
        form = Review2Form()
     return render(request, 'indexReview2.html', {'form': form, 'message': messages} )

def indexTicket(request):
     form = TicketForm(request.POST or None, request.FILES)
     messages = "enregistrement ok"
     if form.is_valid():
        form.save()
        form = TicketForm()
     return render(request, 'indexTicket.html', {'form': form, 'message': messages} )

def indexAbonnement(request):
     form = AbonnementForm(request.POST or None, request.FILES)
     messages = "enregistrement ok"
     if form.is_valid():
        form.save()
        form = AbonnementForm()
     return render(request, 'indexAbonnement.html', {'form': form, 'message': messages} )


def abonnement(request):
    context={'abonnement': Abonnement.objects.all()}
    return render(request, 'abonnement.html', context)

'''
def flux(request):
    context={'flux': Flux.objects.all()}
    return render(request, 'flux.html', context)
'''
def ticket(request):
    context={'ticket': Ticket.objects.all()}
    return render(request, 'ticket.html', context)

def creat_ticket(request):
    context={'ticket': Ticket.objects.all()}
    # Ticket.objects.create()}
    return render(request, 'creat_ticket.html', context)


def enr_ticket(request):
    ticket.save()

