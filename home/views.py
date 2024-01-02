from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def home(request):
    return render(request,'recipe.html')

# recipes/views.py

def submit_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipeName')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        image_url = request.POST.get('image')

        # Save data to the database
        Recipe.objects.create(
            recipe_name=recipe_name,
            ingredients=ingredients,
            instructions=instructions,
            image_url=image_url
        )

    return render(request, 'table.html')


def recipe_table(request):
    recipes = Recipe.objects.all()
    return render(request, 'table.html', {'recipes': recipes})