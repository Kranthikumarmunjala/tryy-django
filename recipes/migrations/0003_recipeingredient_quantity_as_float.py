# Generated by Django 4.1.5 on 2023-10-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity_as_float',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
