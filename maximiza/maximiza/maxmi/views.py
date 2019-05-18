from django.shortcuts import render
from django.http import HttpResponse
from .models import Quem_Somos, Portifolio, Servicos, Clientes
from .forms import Contato


def home(request):
  quemsomos = Quem_Somos.objects.last()
  portifolio = Portifolio.objects.all()
  servicos = Servicos.objects.all()
  clientes = Clientes.objects.all()

  context={
  'quemsomos':quemsomos,
  'portifolio':portifolio,
  'servicos':servicos,
  'clientes':clientes,  
  }
  return render(request,'home.html', context)


