# Generated by Django 4.1.5 on 2023-12-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_foodrecipe_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrecipe',
            name='food_image',
            field=models.ImageField(upload_to='food/media'),
        ),
    ]