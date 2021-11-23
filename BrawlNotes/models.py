from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
# This class holds the player's individual placement in 1v1 at each official tournament.
#   It includes a year attribute for expansion into previous and future years.
class Placements_1(models.Model):
    # This field will hold the year for the event
    #   This is included for future expansion into previous and future years
    #   beyond 2021.
    Year = models.IntegerField()
    # Enum of regions to choose from that limits scope of options
    #   This includes other regions for expansion beyond North American
    #   players after proof of concept.
    REGIONS = (
        # Regions are AUS(Australia), SEA(Southeast Asia), NA(North America)
        #   EU(Europe), SA(South America)
        ('SEA', 'Southeast Asia'),
        ('AUS', 'Australia'),
        ('NA', 'North America'),
        ('EU', 'Europe'),
        ('SA', 'South America'),
    )
    Region = models.CharField(max_length=3, choices=REGIONS)
    # Listed account name from Smash.gg that hosts the bracket of players.
    #   50 characters should hold almost every name.
    #   This is a primary key so the field is set to True
    SmashggName = models.ForeignKey('Player_Registry', on_delete=CASCADE)
    # This holds the power rank for a given player
    PowerRank = models.IntegerField()
    # This is a foreign key referring to the Official_1_Events table
    #   that holds the official names for each event
    EventName = models.ForeignKey('Official_1_Events', on_delete=CASCADE)
    # This contains the placement of this player for the corresponding event
    #   in the previous attribute. It is important to note when a player does not
    #   compete in an event. This will be represented by "N/A."
    Placement = models.CharField(max_length=7)
    # This contains the player's opponents that they lost to in the event.
    #   The format will be "Player1/Player2" since SQLite3 does not have an
    #   ArrayField type to represent a tuple. The / is a delimiter between
    #   player names.
    Losses = models.CharField(max_length=100)

    # This function returns the PowerRank of given object.
    def getPowerRank(self):
        return self.PowerRank

    # This function returns the Placement of given object.
    def getPlacement(self):
        return self.Placement


# This class acts as the player registry to link their Smashgg names on the bracket
#   to their Bralwhalla ID in game and on stat website Corehalla.com
class Player_Registry(models.Model):
    # Enum of regions to choose from that limits scope of options
    #   This includes other regions for expansion beyond North American
    #   players after proof of concept.
    REGIONS = (
        # Regions are AUS(Australia), SEA(Southeast Asia), NA(North America)
        #   EU(Europe), SA(South America)
        ('SEA', 'Southeast Asia'),
        ('AUS', 'Australia'),
        ('NA', 'North America'),
        ('EU', 'Europe'),
        ('SA', 'South America'),
    )
    Region = models.CharField(max_length=3, choices=REGIONS)
    # This field will contain the player's in-game Brawlhalla ID
    #   This will assist in finding the player's details on Corehalla.com
    BrawlhallaID = models.IntegerField()
    # This will contain the player's bracket name on Smashgg and serve
    #   to match their Brawlhalla ID with their Smashgg name.
    SmashggName = models.CharField(max_length=50, primary_key=True)

    #
    def __str__(self):
        return self.SmashggName


# This class holds the year, region, and name of every official Bralwhalla
#   tournament in a given year
class Official_1_Events(models.Model):
    # This field will hold the year for the event
    #   This is included for future expansion into previous and future years
    #   beyond 2021.
    Year = models.IntegerField()
    # Enum of regions to choose from that limits scope of options
    #   This includes other regions for expansion beyond North American
    #   players after proof of concept.
    REGIONS = (
        # Regions are AUS(Australia), SEA(Southeast Asia), NA(North America)
        #   EU(Europe), SA(South America)
        ('SEA', 'Southeast Asia'),
        ('AUS', 'Australia'),
        ('NA', 'North America'),
        ('EU', 'Europe'),
        ('SA', 'South America'),
    )
    Region = models.CharField(max_length=3, choices=REGIONS)
    EventName = models.CharField(max_length=100, primary_key=True)
