from django.db import models

# Create your models here.

class Categoria(models.Model):
    catNombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.catNombre

class Producto(models.Model):
    proCodigo = models.IntegerField(unique=True, null=False)
    proNombre = models.CharField(max_length=50,null=False)
    proPrecio = models.IntegerField(null=False)
    proCategoria = models.ForeignKey (Categoria, on_delete=models.PROTECT)
    proFoto = models.FileField(upload_to='fotos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.proNombre
    