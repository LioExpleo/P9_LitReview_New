from django.contrib import admin

# Register your models here.
from .models import Abonnement, Flux, Ticket, Review

admin.site.register(Abonnement)
admin.site.register(Flux)
admin.site.register(Ticket)
admin.site.register(Review)
