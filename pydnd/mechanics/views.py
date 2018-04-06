from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.forms.models import model_to_dict
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

class LanguageGet(APIView):

    serializer_class = LanguageListSerializer

    def get(self, request, name_or_id):
        return get_language(name_or_id)


def get_language(name_or_id):

    if name_or_id.isdigit():
        queryset = Language.objects.get(id=int(name_or_id))
    else:
        queryset = Language.objects.get(name__iexact=name_or_id)
    return Response(model_to_dict(queryset), status=status.HTTP_200_OK)


class ConditionGet(APIView):

    serializer_class = ConditionListSerializer

    def get(self, request, name_or_id):
        return get_condition(name_or_id)


def get_condition(name_or_id):

    if name_or_id.isdigit():
        queryset = Condition.objects.get(id=int(name_or_id))
    else:
        queryset = Condition.objects.get(name__iexact=name_or_id)
    return Response(model_to_dict(queryset), status=status.HTTP_200_OK)


class DamageTypeGet(APIView):

    serializer_class = DamageTypeListSerializer

    def get(self, request, name_or_id):
        return get_damage_type(name_or_id)


def get_damage_type(name_or_id):

    if name_or_id.isdigit():
        queryset = DamageType.objects.get(id=int(name_or_id))
    else:
        queryset = DamageType.objects.get(name__iexact=name_or_id)
    return Response(model_to_dict(queryset), status=status.HTTP_200_OK)


class MagicSchoolGet(APIView):

    serializer_class = MagicSchoolListSerializer

    def get(self, request, name_or_id):
        return get_magic_school(name_or_id)


def get_magic_school(name_or_id):

    if name_or_id.isdigit():
        queryset = MagicSchool.objects.get(id=int(name_or_id))
    else:
        queryset = MagicSchool.objects.get(name__iexact=name_or_id)
    return Response(model_to_dict(queryset), status=status.HTTP_200_OK)



