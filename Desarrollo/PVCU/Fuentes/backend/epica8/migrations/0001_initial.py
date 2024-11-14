# Generated by Django 5.1.3 on 2024-11-14 02:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Reporte')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'db_table': 'Reporte',
            },
        ),
    ]
