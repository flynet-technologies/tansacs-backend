from django.core.files.base import ContentFile
import base64
from rest_framework import serializers
from jobs.models import SSLC, HSC, UG, PG, Experience, PreferedExperience, Job


class SSLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSLC
        fields = '__all__'
        extra_kwargs = {
            'last_name': {'required': False},
        }


class HSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSC
        fields = '__all__'
        extra_kwargs = {
            'last_name': {'required': False},
        }


class UGSerializer(serializers.ModelSerializer):
    class Meta:
        model = UG
        fields = '__all__'
        extra_kwargs = {
            'last_name': {'required': False},
        }


class PGSerializer(serializers.ModelSerializer):
    class Meta:
        model = PG
        fields = '__all__'
        extra_kwargs = {
            'last_name': {'required': False},
            'job': {'required': False}
        }


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        extra_kwargs = {
            'job': {'required': False}
        }


class PreferedExperienceSerializer(serializers.ModelSerializer):
    NOC = serializers.FileField(allow_empty_file=True, required=False)

    class Meta:
        model = PreferedExperience
        fields = '__all__'
        extra_kwargs = {
            'NOC': {'required': False},
            'job': {'required': False}
        }


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        # No fields are included in the serializer
        fields = ['position', 'sslc', 'hsc', 'ug', 'user']
