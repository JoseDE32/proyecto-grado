# Generated by Django 4.1.2 on 2023-06-02 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_usuario_rol', '0021_act_simultanea_cond_excepcion_discap_men_and_more'),
        ('modulo_instancia', '0006_delete_instancia'),
        ('modulo_programa', '0003_estado_programa_remove_programa_estudiante_estado_and_more'),
        ('modulo_academico', '0003_curso_items_historico_items_semestre_profesores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial_academico_del_estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio_semestral', models.DecimalField(decimal_places=2, max_digits=3)),
                ('promedio_acumulado', models.DecimalField(decimal_places=2, max_digits=3)),
                ('json_materias', models.JSONField(default=dict)),
                ('id_estudiante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='modulo_usuario_rol.estudiante')),
                ('id_programa_estudiante', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='id_programa_estudiante_in_historial_academico_del_estudiante', to='modulo_programa.programa_estudiante')),
                ('id_semestre', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='id_semestre_in_historial_academico_del_estudiante', to='modulo_instancia.semestre')),
            ],
        ),
        migrations.RemoveField(
            model_name='historial_academico',
            name='id_estudiante',
        ),
        migrations.AlterField(
            model_name='historial_academico',
            name='json_materias',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.DeleteModel(
            name='historial_academico_anterior',
        ),
    ]
