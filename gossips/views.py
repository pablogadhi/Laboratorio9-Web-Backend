"""
Viewsets del API
"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models, serializers


class GossipViewSet(viewsets.ModelViewSet):
    """
    Viewset para el modelo de chismes
    """
    queryset = models.Gossip.objects.all()
    serializer_class = serializers.GossipSerializer

    @action(methods=['GET'], detail=True, url_path='description')
    def get_description(self, request, pk=None):
        gossip = models.Gossip.objects.get(pk=pk)
        return Response({
            'description': gossip.description
        })
