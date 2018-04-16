from django.db import models
from pydnd.mechanics.models import Language, MagicSchool
from pydnd.character.models import AbilityScore


class SubRace(models.Model):

    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, related_name="subrace_languages")
    language_options = models.ManyToManyField(Language, null=True, related_name="subrace_language_options")
    desc = models.CharField(max_length=10000)

    # racial_traits =
    # racial_trait_options =
    # ability_bonuses =
    # starting_proficiencies


class Race(models.Model):

    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, related_name="languages")
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


# class SubClass(models.Model):
#
#     pass
#
# class Class(models.Model):
#
#     name = models.CharField(max_length=100, unique=True)
#     hit_die = models.IntegerField()
#     saving_throws = models.ManyToManyField(AbilityScore)
#
#     # proficiencies
#     # starting_equipment
#
#
#     {'', '', 'subclasses',
#      'spellcasting', 'proficiency_choices', 'class_levels',
#      '', '',
#      '', '', '', ''}
