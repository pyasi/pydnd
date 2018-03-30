from rest_framework import generics

from .models import SpecialAbility, Action
from .serializers import SpecialAbilitySerializer, ActionSerializer


# TODO Remove Post ability
class SpecialAbilityList(generics.ListCreateAPIView):

    queryset = SpecialAbility.objects.all()
    serializer_class = SpecialAbilitySerializer


# TODO Remove Post ability
class ActionList(generics.ListCreateAPIView):

    queryset = Action.objects.all()
    serializer_class = ActionSerializer
