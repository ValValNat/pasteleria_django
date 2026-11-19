from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nombre= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    descripcion= models.TextField()
    ingredientes= models.ManyToManyField(
        "Ingrediente",
        through="RecetaIngrediente",
        related_name='recetas'
    )

    def _str__(self):
        return self.descripcion

class Pastel(models.Model):
    nombre= models.CharField(max_length=200)
    precio= models.FloatField()
    receta= models.OneToOneField(
        'Receta',
        related_name='pastel',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.nombre

class RecetaIngrediente(models.Model):
    class Medida(models.TextChoices):
        GRAMOS = "gramos", "Gramos"
        KILOS = "kilos", "Kilos"
        CUCHARADAS = "cucharadas", "Cucharadas"
        LITROS = "litros", "Litros"
        VASOS = "vasos", "Vasos"

    receta= models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='receta_ingrediente'
    )

    ingrediente= models.ForeignKey(
        Ingrediente,
        on_delete=models.CASCADE,
        related_name='receta_ingrediente'
    )

    cantidad=models.IntegerField()

    class Meta:
        unique_together=["receta", "ingrediente"]


    def __str__(self):
        return str(self.cantidad)

    medida=models.CharField(max_length=15, choices=Medida.choices, default=Medida.GRAMOS)
