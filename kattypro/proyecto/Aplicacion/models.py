from django.db import models

# Create your models here.
class Ventas (models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Nombre')
    marca =models.CharField(max_length=100,verbose_name="Marca",null=True)
    tipo =models.CharField(max_length=100,verbose_name="Tipo",null=True)
    imagen =models.ImageField(upload_to='imagen/',verbose_name="Imagen",null=True)

    def delete (self, using=None , keep_parents=False ):
         self.imagen.storage.delete(self.imagen.name)
         super().delete()
   
        


   
   
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=100)
    password= models.CharField(max_length=50)
    nombre =models.CharField(max_length=50)
    tipousu =models.IntegerField()
    
class Registro (models.Model):
    id = models.AutoField(primary_key=True)
    usuario1=models.CharField(max_length=100)
    password1= models.CharField(max_length=50)
    repepaswor=models.CharField(max_length=50)
   