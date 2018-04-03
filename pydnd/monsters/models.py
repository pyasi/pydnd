from django.db import models
from pydnd.skills.models import SpecialAbility, Action, Reaction, LegendaryAction
from pydnd.mechanics.models import Language, Damage_Type, Condition

class Monster(models.Model):

    # TODO Make name unique
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, null=True, blank=True)
    alignment = models.CharField(max_length=500)
    armor_class = models.FloatField(null=True)
    hit_points = models.FloatField(null=True)
    hit_die = models.FloatField(null=True)
    speed = models.CharField(max_length=500)
    senses = models.CharField(null=True, max_length=1000, blank=True)
    languages = models.ManyToManyField(Language, null = True)

    # Attributes
    arcana = models.FloatField(null=True)
    insight = models.FloatField(null=True)
    deception = models.FloatField(null=True)
    intimidation = models.FloatField(null=True)
    perception = models.FloatField(null=True)
    persuasion = models.FloatField(null=True)
    history = models.FloatField(null=True)
    athletics = models.FloatField(null=True)
    survival = models.FloatField(null=True)
    stealth = models.FloatField(null=True)
    investigation = models.FloatField(null=True)
    acrobatics = models.FloatField(null=True)
    performance = models.FloatField(null=True)
    strength = models.FloatField(null=True)
    dexterity = models.FloatField(null=True)
    constitution = models.FloatField(null=True)