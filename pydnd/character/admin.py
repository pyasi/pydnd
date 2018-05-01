from django.contrib import admin
from .models import AbilityScore, Skill, Spell, SpellCastingClass

admin.site.register(AbilityScore)
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(SpellCastingClass)
