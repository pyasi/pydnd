from rest_framework import serializers
from .models import SpecialAbility, Action, Reaction, LegendaryAction


class SpecialAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialAbility
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction
        fields = '__all__'


class LegendaryActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegendaryAction
        fields = '__all__'