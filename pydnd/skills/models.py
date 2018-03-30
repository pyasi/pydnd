from django.db import models


class SpecialAbility(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    damage_bonus = models.FloatField(null=True)
    damage_dice = models.CharField(max_length=20, null=True)
    attack_bonus = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    damage_bonus = models.FloatField(null=True)
    damage_dice = models.CharField(max_length=20, null=True)
    attack_bonus = models.FloatField(null=True)

    def __str__(self):
        return self.name
