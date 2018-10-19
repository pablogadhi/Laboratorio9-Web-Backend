from rest_framework import serializers
from . import models

class GossipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gossip
        fields = ('title', 'description')
