from django.urls import path
from .views import RecipeListView, RecipeCreateView, RecipeUpdateView, RecipeDetailView

urlpatterns = [
  path('recipes/', RecipeListView.as_view(), name='recipe-list'),
  path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
  path('recipes/<uuid:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
  path('recipes/<uuid:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]
