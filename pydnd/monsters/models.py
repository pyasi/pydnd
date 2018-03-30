from django.db import models
from pydnd.skills.models import SpecialAbility, Action


class Monster(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, null=True, blank=True)
    alignment = models.CharField(max_length=100)
    armor_class = models.FloatField()
    hit_points = models.FloatField()
    speed = models.CharField(max_length=50)
    strength = models.FloatField(null=True)
    dexterity = models.FloatField(null=True)
    constitution = models.FloatField(null=True)
    intelligence = models.FloatField(null=True)
    wisdom = models.FloatField(null=True)
    charisma = models.FloatField(null=True)
    medicine = models.FloatField(null=True)
    religion = models.FloatField(null=True)
    damage_vulnerabilities = models.CharField(null=True, max_length=100, blank=True)
    damage_resistances = models.CharField(null=True, max_length=100, blank=True)
    damage_immunities = models.CharField(null=True, max_length=100, blank=True)
    condition_immunities = models.CharField(null=True, max_length=100, blank=True)
    senses = models.CharField(null=True, max_length=100, blank=True)
    languages = models.CharField(null=True, max_length=100, blank=True)
    challenge_rating = models.FloatField(null=True)
    special_abilities = models.ManyToManyField(SpecialAbility, null=True)
    actions = models.ManyToManyField(Action, null=True)

    def __str__(self):
        return self.name
