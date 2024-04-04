# Generated by Django 4.1.13 on 2024-04-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_category_en_food_category_ru_food_category_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='food',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='food',
            name='category_uz',
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
    ]