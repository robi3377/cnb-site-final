# Generated by Django 4.2.1 on 2023-07-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_search_bar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olimpici',
            name='anul',
            field=models.CharField(max_length=255),
        ),
    ]