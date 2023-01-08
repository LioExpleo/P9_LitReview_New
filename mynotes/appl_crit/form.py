from django import forms
from .models import ModelTicket

class Tick(forms.ModelForm):
    class Meta:
        model = ModelTicket
        fields =('title', 'description', 'user', 'image', 'time_created')
