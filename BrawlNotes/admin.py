from django.contrib import admin

# Register your models here.
from .models import Placements_1, Player_Registry, Official_1_Events

admin.site.register(Placements_1)
admin.site.register(Player_Registry)
admin.site.register(Official_1_Events)
