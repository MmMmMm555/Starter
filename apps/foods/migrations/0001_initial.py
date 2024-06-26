# Generated by Django 4.1.13 on 2024-03-28 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Category ',
                'verbose_name_plural': 'Categories ',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('image', models.ImageField(upload_to='foods/', verbose_name='image')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='foods.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Food ',
                'verbose_name_plural': 'Foods ',
            },
        ),
    ]
