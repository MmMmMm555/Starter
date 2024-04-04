# Generated by Django 4.1.13 on 2024-04-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0004_branch_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='address_en',
            field=models.CharField(max_length=200, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='branch',
            name='address_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='branch',
            name='address_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='branch',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='branch',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='branch',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='name'),
        ),
    ]