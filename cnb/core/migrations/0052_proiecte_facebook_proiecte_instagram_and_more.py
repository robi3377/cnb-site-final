# Generated by Django 4.2.1 on 2023-08-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_biblioteca'),
    ]

    operations = [
        migrations.AddField(
            model_name='proiecte',
            name='facebook',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='proiecte',
            name='instagram',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='proiecte',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]