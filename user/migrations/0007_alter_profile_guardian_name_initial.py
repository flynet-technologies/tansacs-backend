# Generated by Django 4.2.7 on 2023-12-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='guardian_name_initial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]