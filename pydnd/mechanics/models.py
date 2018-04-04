from django.db import models

# Create your models here.
class Damage_Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)


class MagicSchool(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    typical_speakers = models.CharField(max_length=100)
    script = models.CharField(max_length=20)

    def __str__(self):
        return self.name
