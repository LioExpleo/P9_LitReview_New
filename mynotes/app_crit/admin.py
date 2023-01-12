from django.contrib import admin

# Register your models here.
from .models import Abonnement, Ticket, Review, Review2

admin.site.register(Abonnement)

admin.site.register(Review)
admin.site.register(Review2)
admin.site.register(Ticket)
