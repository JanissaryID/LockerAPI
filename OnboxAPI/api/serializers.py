from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Lockers, Boxs

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxs
        fields = [
            'NumberBox'
            ]

class LockersSerializer(serializers.ModelSerializer):
    boxs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Lockers
        fields = [
            'IdLocker',
            'QuantityBox',
            'boxs',
        ]