from django.urls import path
from .views import LanguageList, ConditionList, DamageTypeList

urlpatterns = [
    path("language/", LanguageList.as_view(), name="language"),
    path("condition/", ConditionList.as_view(), name="condition"),
    path("damagetype/", DamageTypeList.as_view(), name="damagetype"),
]
