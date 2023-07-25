from django.urls import path
from appTienda import views

urlpatterns = [
    path('categoria', views.CategoriaList.as_view()),
    path('producto', views.ProductoList.as_view()),
    path('categoria/<int:pk>', views.CategoriaDetail.as_view()),
    path('producto/<int:pk>', views.ProductoDetail.as_view()),
    path('producto/codigo/<int:codigo>', views.ProductoPorCodigo.as_view(), name='producto-por-codigo'),
]
