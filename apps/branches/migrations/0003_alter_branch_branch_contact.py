# Generated by Django 4.1.13 on 2024-04-02 13:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_branch_branch_contact_branch_branch_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='branch_contact'),
        ),
    ]
