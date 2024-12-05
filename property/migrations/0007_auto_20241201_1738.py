# Generated by Django 2.2.24 on 2024-12-01 14:38

from django.db import migrations

def is_old_or_new(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)
    

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20241124_2332'),
    ]

    operations = [
        migrations.RunPython(is_old_or_new)
    ]



    
