# Generated by Django 5.1.2 on 2024-10-12 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_alter_turma_periodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.periodo'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.periodo'),
        ),
    ]
