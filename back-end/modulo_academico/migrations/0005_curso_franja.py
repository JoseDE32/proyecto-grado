# Generated by Django 4.1.2 on 2023-06-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_academico', '0004_historial_academico_del_estudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='franja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
