# Generated by Django 3.2.3 on 2025-02-02 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodgram', '0015_auto_20250202_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tokens',
            options={'ordering': ('-created_date',), 'verbose_name': 'Короткая ссылка', 'verbose_name_plural': 'Короткие ссылки'},
        ),
        migrations.AlterField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_favorite', to='foodgram.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_shopping_cart', to='foodgram.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart_recipes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='full_url',
            field=models.URLField(unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='requests_count',
            field=models.IntegerField(default=0, verbose_name='Количество запросов'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='short_link',
            field=models.URLField(blank=True, db_index=True, unique=True, verbose_name='Короткая ссылка'),
        ),
    ]
