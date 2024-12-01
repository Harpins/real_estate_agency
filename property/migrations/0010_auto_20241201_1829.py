# Generated by Django 2.2.24 on 2024-12-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20241201_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='flat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints_on_flat', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]
