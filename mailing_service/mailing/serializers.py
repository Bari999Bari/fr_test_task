from rest_framework import serializers

from .models import Consumer


class ConsumerListSerializer(serializers.ModelSerializer):
    """List of consumers."""

    class Meta:
        model = Consumer
        fields = '__all__'


class ConsumerCreateSerializer(serializers.ModelSerializer):
    """Create consumer."""

    class Meta:
        model = Consumer
        fields = '__all__'
