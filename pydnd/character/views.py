from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.views import APIView

from .models import AbilityScore, Skill
from .serializers import AbilityScoreListSerializer, AbilityScoreSerializer, SkillListSerializer, SkillSerializer


class AbilityScoreList(generics.ListCreateAPIView):

    queryset = AbilityScore.objects.all()
    serializer_class = AbilityScoreSerializer


class SkillList(generics.ListCreateAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        ability_score = get_attribute_by_name(data, 'ability_score', AbilityScore)
        skill = SkillSerializer(data=data)
        if skill.is_valid():
            skill_object = skill.save()
            skill_object.ability_score = ability_score
            skill_object = skill.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(model_to_dict(skill_object), status.HTTP_200_OK)


def get_attribute_by_name(data, attribute_name, model_type):
    attribute_value = data.pop(attribute_name)
    attribute_to_get = attribute_value['name']
    attribute_model = get_object_or_404(model_type, name__iexact=attribute_to_get)
    return attribute_model


class GetAbilityScore(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(AbilityScore, id=int(name_or_id))
        else:
            queryset = get_object_or_404(AbilityScore, name__iexact=name_or_id)
        return Response(model_to_dict(queryset), status.HTTP_200_OK)


class GetSkill(APIView):

    def get(self, request, name_or_id):

        if name_or_id.isdigit():
            queryset = get_object_or_404(Skill, id=int(name_or_id))
        else:
            queryset = get_object_or_404(Skill, name__iexact=name_or_id)

        skill = model_to_dict(queryset)
        ability_score = model_to_dict(get_object_or_404(AbilityScore, id=skill['id']))
        skill['ability_score'] = ability_score

        return Response(skill, status.HTTP_200_OK)
