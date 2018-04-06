from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Monster, Action, SpecialAbility, Reaction, LegendaryAction
from .serializers import MonsterSerializer, MonsterListSerializer
from pydnd.skills.serializers import SpecialAbilitySerializer, ActionSerializer, ReactionSerializer, LegendaryActionSerializer
from pydnd.mechanics.models import Language, Condition, DamageType


# TODO Remove Post ability - Admin required?
class MonsterList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        # TODO make sure it's an auth user

        data = request.data

        # Existing attributes
        languages = get_attribute_by_name(data, 'languages', Language)
        damage_vulnerabilities = get_attribute_by_name(data, 'damage_vulnerabilities', DamageType)
        damage_resistances = get_attribute_by_name(data, 'damage_resistances', DamageType)
        damage_immunities = get_attribute_by_name(data, 'damage_immunities', DamageType)
        condition_immunities = get_attribute_by_name(data, 'condition_immunities', Condition)

        # Created attributes
        abilities = create_attribute(data, 'special_abilities', SpecialAbilitySerializer, SpecialAbility)
        reactions = create_attribute(data, 'reactions', ReactionSerializer, Reaction)
        legendary_actions = create_attribute(data, 'legendary_actions', LegendaryActionSerializer, LegendaryAction)
        actions = create_attribute(data, 'actions', ActionSerializer, Action)

        monster = MonsterSerializer(data=data)
        if monster.is_valid():
            monster_object = monster.save()
        else:
            monster_object = get_object_or_404(Monster, name=monster.initial_data['name'])

        for language in languages:
            monster_object.languages.add(language)
        for damage_vulnerability in damage_vulnerabilities:
            monster_object.damage_vulnerabilities.add(damage_vulnerability)
        for damage_immunity in damage_immunities:
            monster_object.damage_immunities.add(damage_immunity)
        for damage_resistance in damage_resistances:
            monster_object.damage_resistances.add(damage_resistance)
        for condition_immunity in condition_immunities:
            monster_object.condition_immunities.add(condition_immunity)

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


def get_attribute_by_name(data, attribute_name, model_type):
    monster_attributes = []
    try:
        attribute_names = data.pop(attribute_name)
        for attribute in attribute_names:
            try:
                attribute_model = model_type.objects.get(name__iexact=attribute)
                monster_attributes.append(attribute_model)
            except ObjectDoesNotExist:

                #TODO So many that we can't get due to wording.
                print("Couldn't get: {}".format(attribute))
                with open('failures.txt', 'a') as file:
                    file.write("Data: {}, Attribute {}, Issue: {}\n".format(data['index'], attribute_name, attribute))
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

        languages = get_monster_attribute(model, 'languages')
        model['languages'] = languages

        damage_vulnerabilities = get_monster_attribute(model, 'damage_vulnerabilities')
        model['damage_vulnerabilities'] = damage_vulnerabilities

        damage_resistances = get_monster_attribute(model, 'damage_resistances')
        model['damage_resistances'] = damage_resistances

        damage_immunities = get_monster_attribute(model, 'damage_immunities')
        model['damage_immunities'] = damage_immunities

        condition_immunities = get_monster_attribute(model, 'condition_immunities')
        model['condition_immunities'] = condition_immunities

        if attribute:
            return Response(model[attribute], status=status.HTTP_200_OK)
        else:
            return Response(model, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        # TODO should this be an error?
        return Response(None, status=status.HTTP_204_NO_CONTENT)