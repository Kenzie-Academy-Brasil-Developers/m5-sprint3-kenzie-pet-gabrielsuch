# Generated by Django 4.0.5 on 2022-07-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_rename_characteristic_id_animal_characteristic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='characteristic',
            new_name='characteristics',
        ),
    ]
