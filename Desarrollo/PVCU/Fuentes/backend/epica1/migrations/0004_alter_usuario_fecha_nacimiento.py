# Generated by Django 5.1.3 on 2024-11-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica1', '0003_alter_usuario_apellido_m_alter_usuario_apellido_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]