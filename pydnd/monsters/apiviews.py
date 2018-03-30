from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .models import Monster, SpecialAbility, Action
from .serializers import MonsterSerializer, SpecialAbilitySerializer, ActionSerializer


# TODO Remove Post ability - Admin required?
class MonsterList(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):
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


    def delete(self, request):
        Monster.objects.all().delete()
        return Response(status.HTTP_202_ACCEPTED)

    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer


class MonsterGet(APIView):

    serializer_class = MonsterSerializer

    def get(self, request, name_or_id):
        try:
            if name_or_id.isdigit():
                queryset = Monster.objects.get(id=int(name_or_id))
            else:
                queryset = Monster.objects.get(name=name_or_id)
            model = model_to_dict(queryset)

            abilities = []
            for ability in model['special_abilities']:
                abilities.append(model_to_dict(ability))
            model['special_abilities'] = abilities

            actions = []
            for action in model['actions']:
                actions.append(model_to_dict(action))
            model['actions'] = actions

            return Response(model, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            # TODO should this be an error?
            return Response(None, status=status.HTTP_204_NO_CONTENT)


class MonsterActionsList(APIView):

    serializer_class = MonsterSerializer

    def get(self, request, name_or_id):
        try:
            if name_or_id.isdigit():
                queryset = Monster.objects.get(id=int(name_or_id))
            else:
                queryset = Monster.objects.get(name=name_or_id)
            model = model_to_dict(queryset)
            actions = []
            for action in model['actions']:
                actions.append(model_to_dict(action))

            return Response(actions, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            # TODO should this be an error?
            return Response(None, status=status.HTTP_204_NO_CONTENT)

# TODO Remove Post ability
class SpecialAbilityList(generics.ListCreateAPIView):

    queryset = SpecialAbility.objects.all()
    serializer_class = SpecialAbilitySerializer


# TODO Remove Post ability
class ActionList(generics.ListCreateAPIView):

    queryset = Action.objects.all()
    serializer_class = ActionSerializer