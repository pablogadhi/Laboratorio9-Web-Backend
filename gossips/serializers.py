"""
Serializadores del API
"""
from rest_framework import serializers
from . import models


class GossipSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo de chismes
    """
    class Meta:
        model = models.Gossip
        fields = ('id', 'title', 'date')
