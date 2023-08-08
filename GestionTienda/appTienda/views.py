from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.views import APIView
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
    
class ProductoImagen(APIView):
    def post(self, request):
        serializer = Productoserializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            archivo = validated_data['proFoto']
            archivo.name = 'producto.png'
            validated_data['proFoto'] = archivo
            producto = Producto(**validated_data)
            serializer.save()
            serializer_response = Productoserializer(producto)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)