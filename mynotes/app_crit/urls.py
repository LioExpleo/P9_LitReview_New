from app_crit import views
from django.urls import path

urlpatterns =[
	path('abonnement/',views.abonnement, name='abonnement'),
	path('flux/',views.flux, name='flux'),
]


