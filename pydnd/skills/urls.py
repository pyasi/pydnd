from django.urls import path
from .views import SpecialAbilityList, SpecialAbilityGet, ActionList, ActionGet, ReactionList, LegendaryActionList

urlpatterns = [
    path("special_abilities/", SpecialAbilityList.as_view(), name="special_ability"),
    path("special_abilities/<str:name_or_id>/", SpecialAbilityGet.as_view(), name="special_ability"),
    path("actions/", ActionList.as_view(), name="actions"),
    path("actions/<str:name_or_id>/", ActionGet.as_view(), name="actions"),
    path("reactions/", ReactionList.as_view(), name="reactions"),
    path("legendary_actions/", LegendaryActionList.as_view(), name="legendary_actions"),
]
