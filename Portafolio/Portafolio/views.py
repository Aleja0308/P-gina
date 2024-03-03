from django.shortcuts import render

def index(request):
  return render(request, 'index.html', {})

def inicio(request):
  return render(request, 'inicio.html', {})

def portafolio(request):
  return render(request, 'portafolio.html', {})