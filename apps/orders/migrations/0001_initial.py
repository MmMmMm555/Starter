# Generated by Django 4.1.13 on 2024-03-28 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total price')),
                ('payment_type', models.CharField(choices=[('cash', 'cash'), ('card', 'card')], default='cash', max_length=4, verbose_name='payment type')),
                ('state', models.CharField(choices=[('waiting', 'waiting'), ('preparing', 'preparing'), ('delivering', 'delivering')], default='waiting', max_length=10, verbose_name='state')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('delivery_time', models.DurationField(verbose_name='delivery time')),
                ('cooking_time', models.DurationField(verbose_name='cooking time')),
                ('cancelled', models.BooleanField(default=False, verbose_name='cancelled')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='branches.branch', verbose_name='branch')),
            ],
            options={
                'verbose_name': 'Order ',
                'verbose_name_plural': 'Orders ',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='amount')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total price')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foods.food', verbose_name='food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='order')),
            ],
            options={
                'verbose_name': 'Order Item ',
                'verbose_name_plural': 'Order Items ',
            },
        ),
    ]
