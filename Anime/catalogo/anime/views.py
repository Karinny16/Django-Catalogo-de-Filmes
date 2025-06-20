from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime
from .forms import AnimeForm

def lista_animes(request):
    animes = Anime.objects.all()
    return render(request, 'animes/lista.html', {'animes': animes})

def criar_anime(request):  
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_animes')
    else:
        form = AnimeForm()        
    return render(request, 'animes/form_anime.html', {'form': form})

def atualizar_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('lista_animes')
    else:
        form = AnimeForm(instance=anime)
    return render(request, 'animes/form_anime.html', {'form': form})

def deletar_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        anime.delete()
        return redirect('lista_animes')
    return render(request, 'animes/confirmar_exclusao.html', {'anime': anime})
