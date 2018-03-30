from rest_framework import serializers
from .models import Monster, SpecialAbility, Action


class MonsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monster
        fields = '__all__'


class SpecialAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialAbility
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'