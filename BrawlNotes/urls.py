from django.urls import path, reverse_lazy
from . import views

from .models import *

app_name = 'BrawlNotes'
urlpatterns = [
    path('add-player/', views.PlayerAddView.as_view(), name = "BrawlNotes-add-player"),
    path('add-placement/', views.PlacementAddView.as_view(), name = "BrawlNotes-add-placement"),
    path('add-event/', views.EventAddView.as_view(), name = "BrawlNotes-add-event"),
    path('search-placement/', views.placementDetails, name = "BrawlNotes-search-placement"),
    path('index-events/', views.IndexViewEvents.as_view(), name='BrawlNotes-index-events'),
    path('index-players/', views.IndexViewPlayers.as_view(), name='BrawlNotes-index-players'),

]
