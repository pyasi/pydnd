from django.urls import path
from .views import LanguageList, ConditionList, DamageTypeList, MagicSchoolList, LanguageGet, ConditionGet, DamageTypeGet, MagicSchoolGet

urlpatterns = [
    path("languages/", LanguageList.as_view(), name="languages"),
    path("languages/<str:name_or_id>/", LanguageGet.as_view(), name="language_get"),
    path("conditions/", ConditionList.as_view(), name="conditions"),
    path("conditions/<str:name_or_id>/", ConditionGet.as_view(), name="condition_get"),
    path("damage_types/", DamageTypeList.as_view(), name="damagetypes"),
    path("damage_types/<str:name_or_id>/", DamageTypeGet.as_view(), name="damage_type_get"),
    path("magic_schools/", MagicSchoolList.as_view(), name="magicschools"),
    path("magic_schools/<str:name_or_id>/", MagicSchoolGet.as_view(), name="magic_school_get"),
]
