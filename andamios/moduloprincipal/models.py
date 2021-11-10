from django.db import models


# Create your models here-.


andamiostipos = [
    [0, "Andamio de fachada"],
    [1, "Andamio multidireccional"],
    [2, "Torres móviles"],
    [3, "Andamios tubulares"],
    [4, "Andamios colgantes"],
    [5, "Andamio de boriquetas"],
    [6, "Andamio de trabajo"],
    [7, "Andamio de caballete"]
]

class Andamio(models.Model):
    cantidadtotal = models.CharField(max_length=50)
    nombrelote = models.CharField(max_length=50)
    tipoandamio = models.IntegerField(choices=andamiostipos)
    valorhora = models.IntegerField()
    photo = models.ImageField(upload_to="media", null=True)

    def __str__(self):
        return self.nombrelote


tipo = [
    [0, "Empresa"],
    [1, "Particular"]
]

ranking = [
    [0, "bronce"],
    [1, "plata"],
    [2, "oro"],
    [3, "platino"]
]

class Cliente(models.Model):
    nombre = models.CharField(max_length=90)
    tipos = models.IntegerField(choices=tipo)
    clasificacion = models.IntegerField(choices=ranking)

    if clasificacion == 0:
        descuento = 0
    elif clasificacion == 1:
        descuento = 0.05
    elif clasificacion == 2:
        descuento = 0.10
    elif clasificacion == 3:
        descuento = 0.15

    def __str__(self):
        return self.nombre, self.descuento


class Alquiler(models.Model):
    code = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    andamio = models.ForeignKey(Andamio, on_delete=models.PROTECT)
    cantidadlotes = models.IntegerField()
    horasalquiler = models.IntegerField()
    fechareserva = models.DateField()

    def __str__(self):
        return self.code