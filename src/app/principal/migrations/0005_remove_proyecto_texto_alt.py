# Generated by Django 3.1.6 on 2021-02-04 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_proyecto_texto_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='texto_alt',
        ),
    ]