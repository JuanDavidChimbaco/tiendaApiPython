from rest_framework import generics
from appTienda.models import Categoria,Producto
from appTienda.serializers import Categoriaserializer,Productoserializer

# Create your views here.

class CategoriaList(generics.ListCreateAPIView) :
    queryset = Categoria.objects.all()
    serializer_class = Categoriaserializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = Categoriaserializer

class ProductoList(generics.ListCreateAPIView) :
    queryset = Producto.objects.all()
    serializer_class = Productoserializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Producto.objects.all()
    serializer_class = Productoserializer

class ProductoPorCodigo(generics.RetrieveAPIView):
    serializer_class = Productoserializer

    def get_object(self):
        codigo = self.kwargs['codigo']
        return Producto.objects.get(proCodigo=codigo)