from django.db import models

# Create your models here.

class Categoria(models.Model):
    catNombre = models.CharField(max_length=50)

    def __str__ (self):
        return self.catNombre

class Producto(models.Model):
    proCodigo = models.IntegerField(unique=True, null=False)
    proNombre = models.CharField(max_length=50,null=False)
    proPrecio = models.IntegerField(null=False)
    proCategoria = models.ForeignKey (Categoria, on_delete=models.PROTECT)

    def __str__ (self):
        return self.proNombre
    