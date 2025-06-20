from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime.urls')),  # <--- Aqui deve apontar para o módulo de URLs correto do app
]
