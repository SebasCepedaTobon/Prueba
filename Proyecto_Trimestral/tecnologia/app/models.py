from django.db import models

# Create your models here.
class marca(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(marca, on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField()
    imagen=models.ImageField(upload_to="productos", null="True")
    def __str__(self):
        return self.nombre

