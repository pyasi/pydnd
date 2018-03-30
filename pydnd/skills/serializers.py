from rest_framework import serializers
from .models import SpecialAbility, Action


class SpecialAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialAbility
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'
