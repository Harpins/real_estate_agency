# Generated by Django 2.2.24 on 2024-12-01 16:38

from django.db import migrations
import phonenumbers


def normalize_phones(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    flats_iterator = Flats.objects.iterator()
    for flat in flats_iterator:
        raw_number = flat.owners_phonenumber
        parsed_number = phonenumbers.parse(raw_number, 'RU')
        flat.owners_pure_phonenumber = None
        if phonenumbers.is_valid_number(parsed_number):
            flat.owners_pure_phonenumber = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_flat_owners_pure_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_phones)
    ]
