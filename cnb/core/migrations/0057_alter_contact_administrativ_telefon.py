# Generated by Django 4.2.1 on 2023-12-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_alter_poze_poza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_administrativ',
            name='telefon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]