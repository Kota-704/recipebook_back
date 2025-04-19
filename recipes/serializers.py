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

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['id', 'user', 'group', 'title', 'content', 'image_url']
    read_only_fields = ['id']

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id', 'name']
    read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
  group = GroupSerializer(read_only=True)

  class Meta:
    model = User
    fields = ['id', 'name', 'group']
    read_only_fields = ['id']
