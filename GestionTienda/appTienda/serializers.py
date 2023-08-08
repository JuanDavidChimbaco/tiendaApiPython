from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from appTienda.models import Categoria,Producto

class Categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','catNombre')

class Productoserializer(serializers.ModelSerializer):
    proFoto = Base64ImageField(required=False)
    class Meta:
        model = Producto
        fields = '__all__'
