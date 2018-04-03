from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Monster, Action, SpecialAbility, Reaction, LegendaryAction
from .serializers import MonsterSerializer, MonsterListSerializer
from pydnd.skills.serializers import SpecialAbilitySerializer, ActionSerializer, ReactionSerializer, LegendaryActionSerializer


# TODO Remove Post ability - Admin required?
class MonsterList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        # TODO make sure it's an auth user

        data = request.data

        abilities = create_attribute(data, 'special_abilities', SpecialAbilitySerializer, SpecialAbility)
        reactions = create_attribute(data, 'reactions', ReactionSerializer, Reaction)
        legendary_actions = create_attribute(data, 'legendary_actions', LegendaryActionSerializer, LegendaryAction)
        actions = create_attribute(data, 'actions', ActionSerializer, Action)

        monster = MonsterSerializer(data=data)
        if monster.is_valid():
            monster_object = monster.save()
        else:
            monster_object = get_object_or_404(Monster, name=monster.initial_data['name'])
        for ability in abilities:
            monster_object.special_abilities.add(ability)
        for action in actions:
            monster_object.actions.add(action)
        for reaction in reactions:
            monster_object.reactions.add(reaction)
        for legendary_action in legendary_actions:
            monster_object.legendary_actions.add(legendary_action)

        return Response(data, status=status.HTTP_200_OK)

    # TODO remove this
    def delete(self, request):
        Monster.objects.all().delete()
        return Response(None, status.HTTP_202_ACCEPTED)

    queryset = Monster.objects.all()
    serializer_class = MonsterListSerializer


def create_attribute(data, attribute_name, serializer, model_type):
    monster_attributes = []
    try:
        attributes = data.pop(attribute_name)
        for attribute in attributes:
            attribute_model = serializer(data=attribute)
            if attribute_model.is_valid():
                monster_attributes.append(attribute_model.save())
            else:
                monster_attributes.append(get_object_or_404(model_type, name=attribute_model.initial_data['name']))
    except KeyError:
        pass

    return monster_attributes


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
        queryset = Monster.objects.get(name__iexact=name_or_id)
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

        reactions = get_monster_attribute(model, 'reactions')
        model['reactions'] = reactions

        legendary_actions = get_monster_attribute(model, 'legendary_actions')
        model['legendary_actions'] = legendary_actions

        if attribute:
            return Response(model[attribute], status=status.HTTP_200_OK)
        else:
            return Response(model, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        # TODO should this be an error?
        return Response(None, status=status.HTTP_204_NO_CONTENT)