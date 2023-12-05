# Generated by Django 4.2.7 on 2023-11-24 04:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('DOB', models.DateField()),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)])),
                ('aadhar', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=10, validators=[user.validators.validate_phone_number])),
                ('alternate_phone_number', models.CharField(max_length=10, validators=[user.validators.validate_phone_number])),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('profile_image', models.ImageField(upload_to='profile/')),
                ('guardian_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('permanent', 'Permanent'), ('communication', 'Communication')])),
                ('address_line1', models.TextField(max_length=250)),
                ('address_line2', models.TextField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(default='Tamil Nadu', max_length=30)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(validators=[user.validators.validate_pincode])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address', to='user.profile')),
            ],
        ),
    ]