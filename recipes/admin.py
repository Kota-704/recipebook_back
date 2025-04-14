from django.contrib import admin
from .models import User, Group, Recipe, Ingredient, RecipeIngredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  list_display = ('title','user', 'group', 'id')
  search_fields = ('title',)
  list_filter = ('group',)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
  list_display = ('recipe', 'ingredient', 'quantity')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'group')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
  list_display = ('name',)
