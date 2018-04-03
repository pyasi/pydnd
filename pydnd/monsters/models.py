from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from pydnd.skills.models import SpecialAbility, Action
from pydnd.mechanics.models import Language, Damage_Type, Condition
=======
=======
>>>>>>> master
=======
>>>>>>> master
from pydnd.skills.models import SpecialAbility, Action, Reaction, LegendaryAction

>>>>>>> master

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
    intelligence = models.FloatField(null=True)
    wisdom = models.FloatField(null=True)
    charisma = models.FloatField(null=True)
    medicine = models.FloatField(null=True)
    religion = models.FloatField(null=True)
    nature = models.FloatField(null=True)

    # Saves
    charisma_save = models.FloatField(null=True)
    constitution_save = models.FloatField(null=True)
    dexterity_save = models.FloatField(null=True)
    strength_save = models.FloatField(null=True)
    intelligence_save = models.FloatField(null=True)
    wisdom_save = models.FloatField(null=True)
    challenge_rating = models.FloatField(null=True)

    # Immunities, vulnerabilities
    damage_vulnerabilities = models.ManyToManyField(Damage_Type, null = True)
    damage_resistances = models.ManyToManyField(Damage_Type, null = True)
    damage_immunities = models.ManyToManyField(Damage_Type, null = True)
    condition_immunities = models.ManyToManyField(Condition, null = True)

    # ManyToMany Models
    special_abilities = models.ManyToManyField(SpecialAbility, null=True)
    actions = models.ManyToManyField(Action, null=True)
    reactions = models.ManyToManyField(Reaction, null=True)
    legendary_actions = models.ManyToManyField(LegendaryAction, null=True)

    def __str__(self):
        return self.name
