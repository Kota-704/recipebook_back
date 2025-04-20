from django.urls import path
from .views import RecipeListView, RecipeCreateView

urlpatterns = [
  path('recipes/', RecipeListView.as_view(), name='recipe-list'),
  path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
]
