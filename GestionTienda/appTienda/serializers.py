from rest_framework import serializers
from appTienda.models import Categoria,Producto

class Categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class Productoserializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
