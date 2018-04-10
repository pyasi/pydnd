from django.shortcuts import get_object_or_404
from rest_framework import generics, status

from .models import AbilityScore
from .serializers import AbilityScoreListSerializer, AbilityScoreSerializer


#List of all equipment categories
class AbilityScoreList(generics.ListCreateAPIView):

    queryset = AbilityScore.objects.all()
    serializer_class = AbilityScoreListSerializer
