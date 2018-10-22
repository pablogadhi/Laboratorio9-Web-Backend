"""
Modelos de la base de datos que maneja el API
"""

from django.db import models


class Gossip(models.Model):
    """
    Modelo para los chismes
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
