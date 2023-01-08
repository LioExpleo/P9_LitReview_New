from .views import indexReview, abonnement, flux, ticket, creat_ticket
from django.urls import path

urlpatterns =[
	#path('abonnement/',abonnement, name='abonnement'),
	#path('flux/',flux, name='flux'),
	#path('ticket/',ticket, name='ticket'),
	#path('creat_ticket/',creat_ticket, name='ticket'),
	path('Review/', indexReview, name='indexReview')
	# path('Add_ticket/',  form.Tickets_Form, name='add_ticket'),
]



