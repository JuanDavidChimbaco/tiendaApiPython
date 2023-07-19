from django.urls import path
from django.conf.urls import url
from appTienda import views

urlpatterns = [
    url(r"^categoria$", views.CategoriaList.as_view()),
    url(r'^producto$', views.ProductoList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)$', views.CategoriaDetail.as_view()),
    url(r'^producto/(2P<pk>[0-9]+)$', views.ProductoDetail.as_view()),
]
