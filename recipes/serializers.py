from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient, Group, User

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields = ['id', 'name']

class RecipeIngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecipeIngredient
    fields = ['id', 'recipe', 'ingredient', 'quantity']
    read_only_fields = ['id']
