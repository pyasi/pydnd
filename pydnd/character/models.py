from django.db import models


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
