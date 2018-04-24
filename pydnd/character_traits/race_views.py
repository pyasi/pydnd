from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Race, SubRace
from pydnd.mechanics.models import Language
from .serializers import *


class RaceList(generics.ListCreateAPIView):

    queryset = Race.objects.all()
    serializer_class = RaceListSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        subraces = get_attributes_by_name(data, 'subraces', SubRace)
        languages = get_attributes_by_name(data, 'languages', Language)
        language_options = get_attributes_by_name(data, 'language_options', Language)
        race = RaceSerializer(data=data)
        if race.is_valid():
            race_object = race.save()
            for subrace in subraces:
                race_object.subraces.add(subrace)
            for language in languages:
                race_object.languages.add(language)
            for language_option in language_options:
                race_object.language_options.add(language_option)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(race_object), status.HTTP_200_OK)


class GetRace(APIView):

    serializer_class = RaceSerializer

    def get(self, request, name_or_id):

        return respond_to_request(name_or_id, Race)


class SubRaceList(generics.ListCreateAPIView):

    queryset = SubRace.objects.all()
    serializer_class = SubRaceSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        languages = get_attributes_by_name(data, 'languages', Language)
        language_options = get_attributes_by_name(data, 'language_options', Language)
        subrace = SubRaceSerializer(data=data)
        if subrace.is_valid():
            subrace_object = subrace.save()
            for language in languages:
                subrace_object.languages.add(language)
            for language_option in language_options:
                subrace_object.language_options.add(language_option)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(subrace_object), status.HTTP_200_OK)


class GetSubRace(APIView):

    serializer_class = SubRaceSerializer

    def get(self, request, name_or_id):

        return respond_to_request(name_or_id, SubRace)


def get_attributes_by_name(data, attribute_name, model_type):

    attribute_models = []

    try:
        attribute_values = data.pop(attribute_name)
        for attribute in attribute_values:
            attribute_to_get = attribute['name']
            attribute_model = get_object_or_404(model_type, name__iexact=attribute_to_get)
            attribute_models.append(attribute_model)
        return attribute_models
    except:
        return []


def get_object(name_or_id, model_type):

    if name_or_id.isdigit():
        queryset = model_type.objects.get(id=int(name_or_id))
    else:
        queryset = model_type.objects.get(name__iexact=name_or_id)
    return model_to_dict(queryset)


def get_attribute(model, attribute_to_get):

    attributes = []
    for attribute in model[attribute_to_get]:
        attributes.append(model_to_dict(attribute))
    return attributes


def respond_to_request(name_or_id, model_type, attribute_to_get=None):
    try:
        model = get_object(name_or_id, model_type)

        for attribute in ['languages', 'language_options', 'subraces']:
            try:
                attributes = get_attribute(model, attribute)
                model[attribute] = attributes
            except KeyError:
                pass

        if attribute_to_get:
            return Response(model[attribute_to_get], status=status.HTTP_200_OK)
        else:
            return Response(model, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        # TODO should this be an error?
        return Response(None, status=status.HTTP_204_NO_CONTENT)
