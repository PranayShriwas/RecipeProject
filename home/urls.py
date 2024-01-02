from django.urls import path
from .views import submit_recipe, home,recipe_table


urlpatterns = [
    path('', home, name='home'),  
    path('submit_recipe/', submit_recipe, name='submit_recipe'),
    path('recipe_table/', recipe_table, name='recipe_table'),
]
