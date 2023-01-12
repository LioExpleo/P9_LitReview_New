from .views import indexReview, abonnement, ticket, creat_ticket, indexTicket, indexAbonnement, indexReview2
from django.urls import path

urlpatterns =[
	path('CreatAbonnement/',indexAbonnement , name='abonnement'),
	#path('flux/',flux, name='flux'),
	#path('ticket/',ticket, name='ticket'),
	#path('creat_ticket/',creat_ticket, name='ticket'),
	path('CreatReview/', indexReview, name='indexReview'),
	path('CreatReview2/', indexReview2, name='indexReview2'),
	path('CreatTicket/', indexTicket, name='indexTicket')
	# path('Add_ticket/',  form.Tickets_Form, name='add_ticket'),
]



