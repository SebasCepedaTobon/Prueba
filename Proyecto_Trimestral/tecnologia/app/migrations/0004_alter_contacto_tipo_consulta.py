# Generated by Django 3.2.3 on 2021-06-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.CharField(choices=[['consulta', 'consulta'], ['reclamo', 'reclamo'], ['sugerencia', 'sugerencia'], ['felicitaciones', 'felicitaciones']], max_length=30),
        ),
    ]
