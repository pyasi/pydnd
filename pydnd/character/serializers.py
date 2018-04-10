from rest_framework import serializers
from .models import AbilityScore, Skill, Spell


class AbilityScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbilityScore
        fields = '__all__'


class AbilityScoreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbilityScore
        fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class SkillListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'name')


class SpellsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = ('id', 'name')

class SpellsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = '__all__'
