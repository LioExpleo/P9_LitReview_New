from django.shortcuts import render

# Create your views here.
from mynotesapp.models import Note

def home(request):
	context ={'notes': Note.objects.all()}
	return render(request, 'home.html',context)
