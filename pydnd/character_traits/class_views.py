from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Class, SubClass
from pydnd.character.models import Spell, AbilityScore, SpellCastingClass
from .serializers import *


class SubClassList(generics.ListCreateAPIView):

    queryset = SubClass.objects.all()
    serializer_class = SubClassListSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        spells = get_attributes_by_name(data, 'spells', Spell)
        subclass = SubClassSerializer(data=data)
        if subclass.is_valid():
            subclass_object = subclass.save()
            for spell in spells:
                subclass_object.subraces.add(spell)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(subclass_object), status.HTTP_200_OK)


class GetSubClass(APIView):

    serializer_class = SubClassSerializer

    def get(self, request, name_or_id):

        return respond_to_request(name_or_id, SubClass)


class ClassList(generics.ListCreateAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassListSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        saving_throws = get_attributes_by_name(data, 'saving_throws', Spell)
        subclasses = get_attributes_by_name(data, 'subclasses', SubClass)
        spell_casting = get_attributes_by_name(data, 'spell_casting', SpellCastingClass)

        class_model = ClassSerializer(data=data)
        if class_model.is_valid():
            class_object = class_model.save()
            for subclass in subclasses:
                class_object.subraces.add(subclass)
            for saving_throw in saving_throws:
                class_object.subraces.add(saving_throw)
            for spell_casting_group in spell_casting:
                class_object.subraces.add(spell_casting_group)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(class_object), status.HTTP_200_OK)


class GetClass(APIView):

    serializer_class = ClassSerializer

    def get(self, request, name_or_id):

        return respond_to_request(name_or_id, Class)


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

        for attribute in ['spells']:
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
