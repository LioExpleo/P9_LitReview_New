from django.contrib import admin

# Register your models here.
from .models import Abonnement, Flux

admin.site.register(Abonnement)
admin.site.register(Flux)
