# Generated by Django 4.2.1 on 2023-12-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_alter_contact_administrativ_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_administrativ',
            name='telefon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
