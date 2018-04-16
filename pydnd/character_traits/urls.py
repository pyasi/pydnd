from django.urls import path
from .views import *

urlpatterns = [
    path("races/", RaceList.as_view(), name="races"),
    path("subraces/", SubRaceList.as_view(), name="subraces"),
]
