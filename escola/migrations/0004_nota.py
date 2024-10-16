# Generated by Django 5.1.2 on 2024-10-12 16:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_periodo_matricula_periodo_alter_turma_periodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.periodo')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.turma')),
            ],
        ),
    ]
