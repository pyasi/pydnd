from django.db import models
from pydnd.mechanics.models import Damage_Type


# Create your models here.



class WeaponProperty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    weapon_category = models.CharField(max_length=100) #Eg Martial/Simple
    range_type = models.CharField(max_length=100) #Range or Melee
    normal_range = models.IntegerField()
    long_range = models.IntegerField(null=True)
    damage_type = models.ForeignKey(Damage_Type,on_delete=models.CASCADE)
    weight = models.IntegerField()
    properties = models.ManyToManyField(WeaponProperty, null = True)
    damage_die_count = models.IntegerField()
    damage_die = models.IntegerField()
    cost_quantity = models.IntegerField()
    cost_denom = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    armor_category = models.CharField(max_length=100)
    armor_class=models.IntegerField()
    dex_bonus=models.BooleanField()
    armor_bonus=models.IntegerField()
    weight = models.IntegerField()
    str_min=models.IntegerField()
    stealth_dis = models.BooleanField()
    cost_quantity = models.IntegerField()
    cost_denom = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


class EquipmentSubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    equipment_category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=10000)
    equipment_category = models.ForeignKey(EquipmentSubCategory, on_delete=models.CASCADE)
    cost_quantity = models.IntegerField()
    cost_denom = models.CharField(max_length=2)

    def __str__(self):
        return self.name

