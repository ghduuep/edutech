# Generated by Django 5.1.2 on 2024-10-12 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
