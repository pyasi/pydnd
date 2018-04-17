from django.db import models
from pydnd.mechanics.models import Language, MagicSchool
from pydnd.character.models import AbilityScore, SpellCastingClass, Spell


class SubRace(models.Model):

    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, null=True, related_name="subrace_languages")
    language_options = models.ManyToManyField(Language, null=True, related_name="subrace_language_options")
    desc = models.CharField(max_length=10000)

    # racial_traits =
    # racial_trait_options =
    # ability_bonuses =
    # starting_proficiencies

class Race(models.Model):

    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, null=True, related_name="languages")
    language_options = models.ManyToManyField(Language, null=True, related_name="language_options")
    language_desc = models.CharField(max_length=10000, null=True)
    size = models.CharField(max_length=10000)
    size_description = models.CharField(max_length=10000)
    speed = models.CharField(max_length=10000)
    age = models.CharField(max_length=10000)
    alignment = models.CharField(max_length=10000)
    subraces = models.ManyToManyField(SubRace, null=True)

    # ability_bonuses =

    #starting_proficiencies
    #starting_proficiency_options


class SubClass(models.Model):

    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    spells = models.ManyToManyField(Spell, null=True)
    subclass_flavor = models.CharField(max_length=10000)

    # features


class Class(models.Model):

    name = models.CharField(max_length=100, unique=True)
    hit_die = models.IntegerField()
    saving_throws = models.ManyToManyField(AbilityScore)
    subclasses = models.ManyToManyField(SubClass, null=True)
    spell_casting = models.ManyToManyField(SpellCastingClass, null=True)


    # proficiencies
    # starting_equipment
    # proficiency_choices
    # class_levels
