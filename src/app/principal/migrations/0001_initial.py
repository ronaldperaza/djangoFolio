# Generated by Django 3.1.6 on 2021-02-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenid', models.TextField()),
                ('resumen', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
