# Generated by Django 5.1.3 on 2024-11-14 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica1', '0002_alter_usuario_fecha_nacimiento'),
        ('epica2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido_m',
            field=models.CharField(default='Morales', max_length=200, verbose_name='Apellido materno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_p',
            field=models.CharField(default='Gutierrez', max_length=200, verbose_name='Apellido paterno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.CharField(default='999888777', max_length=20, verbose_name='Celular'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(default='2001-11-11', verbose_name='Fecha de nacimiento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_escuela',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='epica2.escuelaprofesional', verbose_name='Escuela Profesional'),
            preserve_default=False,
        ),
    ]