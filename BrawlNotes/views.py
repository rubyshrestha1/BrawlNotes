from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Player_Registry, Official_1_Events, Placements_1

def index(request):
    return HttpResponse("Hello. You're at the BrawlNotes index.")



