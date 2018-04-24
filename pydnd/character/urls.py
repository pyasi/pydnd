from django.urls import path
from .views import AbilityScoreList, SkillList, GetAbilityScore, GetSkill, SpellList, GetSpell, SpellCastingList, GetSpellCasting

urlpatterns = [
    path("ability_scores/", AbilityScoreList.as_view(), name="ability_scores"),
    path("ability_scores/<str:name_or_id>/", GetAbilityScore.as_view(), name="ability_scores"),
    path("skills/", SkillList.as_view(), name="skills"),
    path("skills/<str:name_or_id>/", GetSkill.as_view(), name="skills"),
    path("spells/", SpellList.as_view(), name="spells"),
    path("spells/<str:name_or_id>/", GetSpell.as_view(), name="spells"),
    path("spell_casting/", SpellCastingList.as_view(), name="spell_casting"),
    path("spell_casting/<str:name_or_id>/", GetSpellCasting.as_view(), name="spell_casting"),
]
