from django.db import models
from pydnd.mechanics.models import MagicSchool


class AbilityScore(models.Model):

    name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.full_name


class Skill(models.Model):

    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    ability_score = models.ForeignKey(AbilityScore, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Spell(models.Model):

    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    higher_level = models.CharField(max_length=10000, null=True)
    range = models.CharField(max_length=1000)
    components = models.CharField(max_length=1000)
    ritual = models.CharField(max_length=10000)
    duration = models.CharField(max_length=1000)
    concentration = models.CharField(max_length=1000)
    casting_time = models.CharField(max_length=1000)
    level = models.IntegerField()
    school = models.ForeignKey(MagicSchool, on_delete=models.CASCADE, null=True)


class SpellCasting(models.Model):

    name = models.CharField(max_length=100, unique=True)