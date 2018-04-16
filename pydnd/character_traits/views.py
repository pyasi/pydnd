from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.views import APIView

from .models import Race, SubRace
from .serializers import *


class RaceList(generics.ListCreateAPIView):

    queryset = Race.objects.all()
    serializer_class = RaceListSerializer


class SubRaceList(generics.ListCreateAPIView):

    queryset = SubRace.objects.all()
    serializer_class = SubRaceListSerializer

