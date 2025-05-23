# Generated by Django 5.2 on 2025-04-14 12:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='グループ名')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='材料名')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='料理名')),
                ('content', models.TextField(max_length=5000, verbose_name='作り方')),
                ('image_url', models.URLField(verbose_name='TOP画像')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.group', verbose_name='グループ')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50, verbose_name='分量（例：100g、1個など）')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='recipes.ingredient', verbose_name='材料')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='recipes.recipe', verbose_name='レシピ')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='recipes.group', verbose_name='グループID')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.user', verbose_name='投稿者'),
        ),
    ]
