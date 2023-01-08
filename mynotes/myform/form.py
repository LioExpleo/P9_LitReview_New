from django import forms
from .models import Products, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =('name', 'firstname', 'email', 'message', 'actif')



