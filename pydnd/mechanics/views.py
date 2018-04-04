from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Language, Condition, DamageType
from .serializers import LanguageSerializer, ConditionSerializer, DamageTypeSerializer


