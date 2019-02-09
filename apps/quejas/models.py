from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    '''Clase Categoria para cada una de las quejas'''
    nombre_categoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    slug_categoria = models.SlugField(max_length=30)


    def __str__(self):
        return self.nombre_categoria

    def __unicode__(self):
        return self.nombre_categoria

class Queja(models.Model):
    '''Clase Queja que son cada una de las quejas que se publicaran en la app'''
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    calificacion = models.IntegerField(blank=True, null=True, default=0)
    categorias = models.ManyToManyField(Categoria)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    '''Clase Comentario donde cada comentario sera dirigido a una publicacion'''
    cuerpo = models.CharField(max_length=150)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey(Queja, on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    calificacion = models.IntegerField(blank=True, null=True, default=0)


    def __str__(self):
        return self.cuerpo

    def __unicode__(self):
        return self.cuerpo
