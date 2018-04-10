from django.contrib import admin
from .models import Language, DamageType, Condition, MagicSchool

admin.site.register(Language)
admin.site.register(DamageType)
admin.site.register(Condition)
admin.site.register(MagicSchool)
