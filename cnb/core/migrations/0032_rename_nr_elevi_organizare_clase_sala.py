# Generated by Django 4.2.1 on 2023-06-08 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_organizare_clase_clasa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizare_clase',
            old_name='nr_elevi',
            new_name='sala',
        ),
    ]
