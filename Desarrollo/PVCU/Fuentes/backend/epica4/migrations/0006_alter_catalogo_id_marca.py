# Generated by Django 5.1.3 on 2024-11-14 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica4', '0005_alter_catalogo_options_articulo_id_marca_and_more'),
        ('epica5', '0003_alter_membresia_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='id_marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epica5.marca', verbose_name='Marca'),
        ),
    ]
