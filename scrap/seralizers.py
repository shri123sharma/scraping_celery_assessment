# serializers.py
from rest_framework import serializers
from .models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobData
        fields ="__all__"
