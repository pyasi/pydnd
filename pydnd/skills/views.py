from rest_framework import generics, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import SpecialAbility, Action, Reaction, LegendaryAction
from .serializers import SpecialAbilitySerializer, ActionSerializer, ReactionSerializer, LegendaryActionSerializer


# TODO Remove Post ability
class SpecialAbilityList(generics.ListCreateAPIView):

    queryset = SpecialAbility.objects.all()
    serializer_class = SpecialAbilitySerializer


class SpecialAbilityGet(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        try:
            name_or_id = self.kwargs['name_or_id']
        except KeyError:
            return Response(status.HTTP_400_BAD_REQUEST)

        if name_or_id.isdigit():
            ability = get_object_or_404(SpecialAbility, id=int(name_or_id))
        else:
            ability = get_object_or_404(SpecialAbility, name__iexact=name_or_id)

        return Response(model_to_dict(ability), status.HTTP_200_OK)

    serializer_class = SpecialAbilitySerializer


# TODO Remove Post ability
class ActionList(generics.ListCreateAPIView):

    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionGet(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        try:
            name_or_id = self.kwargs['name_or_id']
        except KeyError:
            return Response(status.HTTP_400_BAD_REQUEST)

        if name_or_id.isdigit():
            action = get_object_or_404(Action, id=int(name_or_id))
        else:
            action = get_object_or_404(Action, name__iexact=name_or_id)

        return Response(model_to_dict(action), status.HTTP_200_OK)

    serializer_class = SpecialAbilitySerializer


class ReactionList(generics.ListAPIView):

    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class LegendaryActionList(generics.ListAPIView):

    queryset = LegendaryAction.objects.all()
    serializer_class = LegendaryActionSerializer

