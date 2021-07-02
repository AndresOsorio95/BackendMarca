# Generated by Django 3.2.4 on 2021-06-25 01:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_corto', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=50)),
                ('capacidad_maxima', models.PositiveIntegerField(default=0)),
                ('capacidad_disponible', models.PositiveIntegerField(default=0)),
                ('direccion', models.CharField(max_length=80)),
                ('numero_telefonico', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]