import base64
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
    
    def create(self, request, *args, **kwargs):
        archivo = request.data.get('proFoto')
        if archivo:
            # Lee el contenido del archivo en memoria
            file_content = archivo.read()
            # Codifica el contenido en base64
            base64_content = base64.b64encode(file_content).decode('utf-8')
            # Reemplaza el archivo con el contenido en base64
            request.data['proFoto'] = base64_content
        return super().create(request, *args, **kwargs)

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
            producto = serializer.save()
            serializer_response = Productoserializer(producto)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)