# Generated by Django 4.2.7 on 2023-12-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='Experience/'),
        ),
        migrations.AlterField(
            model_name='hsc',
            name='marksheet',
            field=models.FileField(blank=True, null=True, upload_to='HSC/'),
        ),
        migrations.AlterField(
            model_name='pg',
            name='marksheet',
            field=models.FileField(blank=True, null=True, upload_to='PG/'),
        ),
        migrations.AlterField(
            model_name='preferedexperience',
            name='NOC',
            field=models.FileField(blank=True, null=True, upload_to='NOC/'),
        ),
        migrations.AlterField(
            model_name='preferedexperience',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='PreferedExperience/'),
        ),
        migrations.AlterField(
            model_name='sslc',
            name='marksheet',
            field=models.FileField(blank=True, null=True, upload_to='SSLC/'),
        ),
        migrations.AlterField(
            model_name='ug',
            name='marksheet',
            field=models.FileField(blank=True, null=True, upload_to='UG/'),
        ),
    ]
