from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request,'home.html',{'usuario': 'de droga'})



#from .forms import Contatos  #----->usar isso quando for colocar no template



# Create your views here.
