from django.db import models
from epica1.models import Usuario

class Marca(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name = "Dueño")
    nombre = models.CharField("Nombre", max_length = 50, unique = True)
    descripcion = models.CharField("Informacion", max_length = 300)
    logo = models.URLField("Logo")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "Marca"


class Plan(models.Model):
    nombre = models.CharField("Nombre", max_length = 50, unique = True)
    descripcion = models.CharField("Informacion", max_length = 300)
    espacio_extra = models.IntegerField("Espacio adicional")
    duracion = models.IntegerField("Duración en meses")
    precio = models.FloatField("Precio")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"
        db_table = "Plan"


class Membresia(models.Model): #Esta es la tabla MarcaPlan, pero con un nombre menos aburrido
    id_marca = models.ForeignKey(Marca, on_delete = models.CASCADE, verbose_name = "Marca")
    id_plan = models.ForeignKey(Plan, on_delete = models.CASCADE, verbose_name = "Tipo de plan")
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_final = models.DateTimeField()

    def __str__(self):
        return self.id_marca.nombre + ' - ' + self.id_plan.nombre + ' : ' + str(self.fecha_inicio)
    
    class Meta:
        verbose_name = "Membresia"
        verbose_name_plural = "Membresias"
        db_table = "Membresia"