from django.contrib import admin
from .models import SpecialAbility, Action, LegendaryAction, Reaction

admin.site.register(SpecialAbility)
admin.site.register(Action)
admin.site.register(LegendaryAction)
admin.site.register(Reaction)
