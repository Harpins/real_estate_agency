# Generated by Django 2.2.24 on 2024-12-01 14:38

from django.db import migrations

def is_old_or_new(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20241124_2332'),
    ]

    operations = [
        migrations.RunPython(is_old_or_new)
    ]



    