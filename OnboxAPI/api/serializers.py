from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Lockers


class LockersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lockers
        fields = [
            'IdLocker',
            'QuantityBox'
        ]