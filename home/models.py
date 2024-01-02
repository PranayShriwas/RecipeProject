# recipes/models.py

from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.recipe_name
