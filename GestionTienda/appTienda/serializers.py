from rest_framework import serializers
from appTienda.models import Categoria,Producto

class Categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','catNombre', 'catFoto', 'created at', 'updated_at')

class Productoserializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','proCodigo', 'proNombre', 'proPrecio', "proCategoria",
        'profoto', 'created at', 'updated_at')
