from django.urls import path
'''
from .views import tick
urlpatterns=[
    path('tick/', tick, name='tick')
]
'''

from django.urls import path
from mynotes.myform.views import import contact

urlpatterns=[
    path('contact/', contact, name = 'contact')
]
