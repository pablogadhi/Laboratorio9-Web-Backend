from rest_framework import viewsets
from . import models, serializers

# Create your views here.


class GossipViewSet(viewsets.ModelViewSet):
    queryset = models.Gossip.objects.all()
    serializer_class = serializers.GossipSerializer
