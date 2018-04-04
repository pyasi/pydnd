from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Language, Condition, DamageType, MagicSchool
from .serializers import LanguageListSerializer, ConditionListSerializer, DamageTypeListSerializer, MagicSchoolListSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset =  Language.objects.all()
    serializer_class =  LanguageListSerializer

class ConditionList(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionListSerializer


class DamageTypeList(generics.ListCreateAPIView):
    queryset = DamageType.objects.all()
    serializer_class = DamageTypeListSerializer

class MagicSchoolList(generics.ListCreateAPIView):
    queryset = MagicSchool.objects.all()
    serializer_class = MagicSchoolListSerializer
