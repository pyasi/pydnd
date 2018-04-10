from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import AbilityScore, Skill
from .serializers import AbilityScoreListSerializer, AbilityScoreSerializer, SkillListSerializer, SkillSerializer


class AbilityScoreList(generics.ListCreateAPIView):

    queryset = AbilityScore.objects.all()
    serializer_class = AbilityScoreListSerializer


class SkillList(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillListSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        ability_score = get_attribute_by_name(data, 'ability_score', AbilityScore)
        skill = SkillSerializer(data=data)
        if skill.is_valid():
            skill_object = skill.save()
        else:
            skill_object = get_object_or_404(Skill, name=skill.initial_data['name'])

        skill_object.ability_score = ability_score

        return Response(model_to_dict(skill_object), status.HTTP_200_OK)


def get_attribute_by_name(data, attribute_name, model_type):
    attribute_value = data.pop(attribute_name)
    attribute_to_get = attribute_value['name']
    attribute_model = get_object_or_404(model_type, name__iexact=attribute_to_get)
    return attribute_model
