from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Player_Registry, Official_1_Events, Placements_1

"""This class is used to create PlayerAddView.This view inherits a generic View type of CreateView
 in order to add new players to the model Player_Registry in database. Decorator method_decorator is used in the class
 that requires user to add players into the system."""
@method_decorator(login_required, name = 'dispatch')
class PlayerAddView(generic.CreateView):
    model = Player_Registry
    fields = "__all__"
    success_url = reverse_lazy("BrawlNotes:BrawlNotes-add-player")

"""This class is used to create PlacementAddView.This view inherits a generic View type of CreateView
 in order to add new placement to the model Placements_1 in database. Decorator method_decorator is used in the class
 that requires user to log in to add placements into the system."""
@method_decorator(login_required, name = 'dispatch')
class PlacementAddView(generic.CreateView):
    model = Placements_1
    fields = "__all__"
    success_url = reverse_lazy("BrawlNotes:BrawlNotes-add-placement")

"""This class is used to create EventAddView.This view inherits a generic View type of CreateView
 in order to add new events to the model Official_1_Events in database. Decorator method_decorator is used in the class
 that requires user to sign in to add events into the system."""
@method_decorator(login_required, name = 'dispatch')
class EventAddView(generic.CreateView):
    model = Official_1_Events
    fields = "__all__"
    success_url = reverse_lazy("BrawlNotes:BrawlNotes-add-event")

"""This function defines the view to display the data in Placements_1 table. It takes in request from user and
gets all objects of table as result. Then the results are rendered in specified template 'BrawlNotes/search-placement.html'.
The third argument is context.It is the dictionary of values to add to the template context. Decorator login_required
 is used in the class to require user to first log in to view the placement."""
@login_required
def placementDetails(request):
    result = Placements_1.objects.all()
    return render(request, 'BrawlNotes/search-placement.html', {"Placements_1" :result} )

"""This class inherits a generic view of type ListView to display the data of Official_1_Events model."""
class IndexViewEvents(generic.ListView):
    model = Official_1_Events
    template_name = 'BrawlNotes/indexEvent.html'
    context_object_name = 'event_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

"""This class inherits a generic view of type ListView to display the data of Player_Registry model.
Decorator method_decorator is used in the class that requires user to sign in to view players of the system"""
@method_decorator(login_required, name = 'dispatch')
class IndexViewPlayers(generic.ListView):
    model = Player_Registry
    template_name = 'BrawlNotes/indexPlayer.html'
    context_object_name = 'player_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




