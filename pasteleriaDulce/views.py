from django.shortcuts import render
from .models import Pastel, Receta, RecetaIngrediente, Ingrediente

# Create your views here.
def principal(request):
    pasteles= Pastel.objects.all()
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'pasteleriaDulce/principal.html',  {
            'pasteles': pasteles,
            'recetas': recetas,
            'ingredientes': ingredientes
        })