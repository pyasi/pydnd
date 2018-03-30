from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .models import Monster
from .serializers import MonsterSerializer, MonsterListSerializer
from pydnd.skills.serializers import SpecialAbilitySerializer, ActionSerializer


# TODO Remove Post ability - Admin required?
class MonsterList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        # TODO make sure it's an auth user

        data = request.data

        special_abilities = data.pop('special_abilities')
        abilities = []
        for ability in special_abilities:
            special_ability = SpecialAbilitySerializer(data=ability)
            if special_ability.is_valid():
                abilities.append(special_ability.save())

        actions = data.pop('actions')
        monster_actions = []
        for action in actions:
            action = ActionSerializer(data=action)
            if action.is_valid():
                monster_actions.append(action.save())

        monster = MonsterSerializer(data=data)
        if monster.is_valid():
            monster_object = monster.save()
            for ability in abilities:
                monster_object.special_abilities.add(ability)
            for action in monster_actions:
                monster_object.actions.add(action)
        return Response(data, status=status.HTTP_200_OK)

    # TODO remove this
    def delete(self, request):
        Monster.objects.all().delete()
        return Response(None, status.HTTP_202_ACCEPTED)

    queryset = Monster.objects.all()
    serializer_class = MonsterListSerializer


class MonsterGet(APIView):

    serializer_class = MonsterSerializer

    def get(self, request, name_or_id):
        return respond_to_monster_request(name_or_id)


class MonsterActionsList(APIView):

    serializer_class = MonsterSerializer

    def get(self, request, name_or_id):
        return respond_to_monster_request(name_or_id, attribute='actions')


class MonsterSpecialAbilityList(APIView):

    serializer_class = MonsterSerializer

    def get(self, request, name_or_id):
        return respond_to_monster_request(name_or_id, attribute='special_abilities')


# HELPER METHODS


def get_monster(name_or_id):

    if name_or_id.isdigit():
        queryset = Monster.objects.get(id=int(name_or_id))
    else:
        queryset = Monster.objects.get(name=name_or_id)
    return model_to_dict(queryset)


def get_monster_attribute(model, attribute_to_get):

    attributes = []
    for attribute in model[attribute_to_get]:
        attributes.append(model_to_dict(attribute))
    return attributes


def respond_to_monster_request(name_or_id, attribute=None):
    try:
        model = get_monster(name_or_id)

        special_abilities = get_monster_attribute(model, 'special_abilities')
        model['special_abilities'] = special_abilities

        actions = get_monster_attribute(model, 'actions')
        model['actions'] = actions

        if attribute:
            return Response(model[attribute], status=status.HTTP_200_OK)
        else:
            return Response(model, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        # TODO should this be an error?
        return Response(None, status=status.HTTP_204_NO_CONTENT)