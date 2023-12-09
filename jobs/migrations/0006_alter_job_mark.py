# Generated by Django 4.2.7 on 2023-12-07 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_experience_job_pg_job_preferedexperience_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='mark',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]