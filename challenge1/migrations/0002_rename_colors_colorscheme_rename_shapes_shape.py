# Generated by Django 5.0.3 on 2024-03-23 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='ColorScheme',
        ),
        migrations.RenameModel(
            old_name='Shapes',
            new_name='Shape',
        ),
    ]
