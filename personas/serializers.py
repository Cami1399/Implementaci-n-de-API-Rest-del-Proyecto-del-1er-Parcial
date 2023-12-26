from personas.models import Libro, Presentacion, Categoria
from rest_framework import serializers


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['url','id','titulo', 'autor', 'Presentacion', 'Categoria', 'fecha_publicacion', 'sinopsis', 'disponibilidad']

class PresentacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['url', 'id','Presentacion']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['url','id','Categoria']