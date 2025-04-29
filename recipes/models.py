from django.db import models
import uuid
from datetime import date


class Ingredient(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID")
  name=models.CharField(max_length=60, verbose_name="材料名")

class Recipe(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID")
  user=models.ForeignKey(
    "User",
    on_delete=models.CASCADE,
    related_name="recipes",
    # 本番適用時に外す-----
    null=True, blank=True,
    # -----
    verbose_name="投稿者"
  )
  group=models.ForeignKey(
    "Group",
    on_delete=models.CASCADE,
    related_name="recipes",
    # 本番適用時に外す-----
    null=True, blank=True,
    # -----
    verbose_name="グループ"
  )
  title=models.CharField(max_length=60, verbose_name="料理名")
  content=models.TextField(max_length=5000, verbose_name="作り方")
  image_url=models.URLField(verbose_name="TOP画像", null=True, blank=True,)

class RecipeIngredient(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID")
  recipe=models.ForeignKey(
    "Recipe",
    on_delete=models.CASCADE,
    related_name="recipe_ingredients",
    verbose_name="レシピ"
  )
  ingredient=models.ForeignKey(
    "Ingredient",
    on_delete=models.CASCADE,
    related_name="recipe_ingredients",
    verbose_name="材料"
  )
  quantity=models.CharField(max_length=50, verbose_name="分量（例：100g、1個など）")

class Group(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID")
  name=models.CharField(max_length=50, verbose_name="グループ名")

class User(models.Model):
  id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID")
  group=models.ForeignKey(
    "Group",
    on_delete=models.CASCADE,
    related_name="users",
    verbose_name="グループID"
  )
  name=models.CharField(max_length=50, verbose_name="名前")
