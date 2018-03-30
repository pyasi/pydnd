from django.contrib import admin

from .models import Monster, SpecialAbility, Action

admin.site.register(Monster)
admin.site.register(SpecialAbility)
admin.site.register(Action)
