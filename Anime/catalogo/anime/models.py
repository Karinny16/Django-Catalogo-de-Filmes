from django.db import models

# Create your models here.
class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.TextField()
    sinopse = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField(max_length=50 )
    capa= models.TextField(default="")

    def __str__(self):
        return self.titulo