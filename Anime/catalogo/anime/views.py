from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Anime

def lista_animes(request):
    animes = Anime.objects.all()
    return render(request, 'animes/lista.html', {'animes': animes})