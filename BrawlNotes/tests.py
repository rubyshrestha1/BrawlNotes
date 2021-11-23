import unittest

from django.test import TestCase
from .models import Player_Registry, Official_1_Events, Placements_1
from parameterized import parameterized, parameterized_class
from django.urls import reverse
from django.test import Client

"""
This class is the test for Player_Registry table in database. It has three different functions to test three 
attributes of the table. In each function, a new object is created by calling constructor. Then assertEqual method
 is used to test whether the result matches with expected result"""
class PlayerRegistryTest(TestCase):
    """This function tests the region field of the PlayerRegistry table. A new player object is created
    with NorthAmerica, 123 and Moon as Region, BrawlhallaID and SmashggName respectively. The function then asserts if
    the object's 'Region' field matches with the given value, which in this case it should pass. If they do not match,
    message that says 'Region is not
    same' is displayed."""
    def test1_region_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=123, SmashggName="Moon")
        self.assertEqual("North America", player1.Region, msg="Region is not same")  # pass

    """This function tests error region field of the PlayerRegistry table. A new player object is created 
       with NorthAmeri, 123 and Moon as Region, BrawlhallaID and SmashggName respectively. The function then asserts if
       the object's 'Region' field matches with the given value, which in case should fail. If they do not match, 
       message that says 'Region is not same' is displayed."""
    @unittest.expectedFailure
    def test2_region_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=123, SmashggName="Moon")
        self.assertEqual("North Ameri", player1.Region, msg="Region is not same")  # fail

    """This function tests error in region field of the PlayerRegistry table. A new player objects is created with 
        NorthAmerica, "200" and test  as Region, BrawlhallaID and SmashggName respectively.
         The function then asserts if the object's 'BrawlHallaID' field matches with the given ID value. The test fails
          in this case as type of BrawlHallaIDs are not consistent """
    @unittest.expectedFailure
    def test_type_BrawlhallaID_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        self.assertEqual("200", player1.BrawlhallaID, msg="BrawlhallaID is not the same")  # Fail

    """This function tests the region field of the PlayerRegistry table. A new player objects is created with 
        NorthAmerica, 111 and test  as Region, BrawlhallaID and SmashggName respectively.
         The function then asserts if the object's 'BrawlHallaID' field matches with the given ID value. """
    def test_BrawlhallaID_field(self):
            player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
            self.assertEqual(111, player1.BrawlhallaID, msg="BrawlhallaID is not the same")  # Pass

    """This function tests error SmashggName field of the PlayerRegistry table. Two new player objects are created with 
           different region, BrawlHallaID and SmashggName. This function asserts if the 
           'SmashggName' field of same object matches. """
    @unittest.expectedFailure
    def test_SmashggName_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        player2 = Player_Registry.objects.create(Region="South America", BrawlhallaID=101, SmashggName="test1")
        self.assertIs(player1, player2, msg="They do not refer to the same object") # Fail


    """This function tests error in SmashggName field of the PlayerRegistry table. Two new player objects are created with 
        different region and BrawlHalla ID but same SmashggName. Since SmashggName is primary key, it should not allow 
        creation of two objects with same SmashggName. As expected, this test raises integrity error."""
    @unittest.expectedFailure
    def test_integrityError_SmashggName_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        player2 = Player_Registry.objects.create(Region="South America", BrawlhallaID=100, SmashggName="test")

    '''This function tests that the maximum length for the CharField representing a player's SmashggName is 50. A loop is traversed
        more than 50 times and each time a character is appended to a string that will eventually be greater than length 50. This
        string is then used as the SmashggName for the newly created player object. Because the CharField in the Player_Registry table
        has a max length of 50, it should not allow the player object to be created. As expected this test raises an error'''
    @unittest.expectedFailure
    def test_SmashggName_Length(self):
        name = ""
        for i in range(52):
            name+=i
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName=name)





"""
This class is the test for Official_1_Events table in database.setUpTestData function is used which 
helps to initialize certain objects and store them into test database. It has two other functions to
 test eventName and Year field of Official_1_Events table"""
class OfficialEventsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        player2 = Player_Registry.objects.create(Region="North America", BrawlhallaID=0000, SmashggName="Phoenix")
        Official_1_Events.objects.create(Year=2020, Region="North America", EventName="October Championship")
        Official_1_Events.objects.create(Year=2021, Region="North America", EventName="Winter Championship")

    # This functions gets the object created from setUpTestData and checks if eventName matches the given eventName.
    def test_eventName_field(self):
        event1 = Official_1_Events.objects.get(EventName="October Championship")
        self.assertEqual('October Championship', event1.EventName)

    # This function tests the possible error on obtaining the eventName from OfficialEvents.
    # This functions tries to get the object created from setUpTestData using get method.
    # However, the function gives "object does not exist error" because with get method it is trying to
    # access something that has not been created at all.
    @unittest.expectedFailure
    def test_objectError_eventName_field(self):
        event2 = Official_1_Events.objects.get(EventName="November Championship")


    # This functions gets the object created from setUpTestData and checks if year matches the given year.
    def test_Year_field(self):
        event1 = Official_1_Events.objects.get(Year=2021)
        self.assertEqual(2021, event1.Year, msg="The year is not equal to 2021")

    '''This function tests that the maximum length for the CharField representing an event's name is 100. A loop is traversed
        more than 100 times and each time a character is appended to a string that will eventually be greater than length 100. This
        string is then used as the EventName for the newly created event object. Because the CharField in the Official_1_Events table
        has a max length of 100, it should not allow the player object to be created. As expected this test raises an error'''
    @unittest.expectedFailure
    def test_EventName_length(self):
        name = ""
        for i in range(103):
            name+=i
        eventSample = Official_1_Events.objects.create(Year=2021, Region="North America", EventName=name)

"""
This class performs the parameterized test for one of the attributes of Placement_1 table in database. 
It uses @parameter.expand to take in array of tuples of input and output. It creates a new function for each 
tuple to check the input and output. For example: there are two tuples in array. So, @parameterized.expand
creates test_PowerRank_field_0 and test_PowerRank_field_1 as the function to perform tests."""
class PlacementsTest(TestCase):
    @parameterized.expand([
        (1, 1),
        (5, 5)
    ])
    # This function tests the PowerRank field of Placement_1 table. It creates an object of table with the
    # given input PowerRank
    # and then uses self.assertEqual to check if
    def test_PowerRank_field(self, input, expected):
        rank = Placements_1(PowerRank=input)
        self.assertEqual(rank.getPowerRank(), expected)

"""
This class performs the parameterized test to test for error for one of the attributes of Placement_1 table in database. 
It uses @parameter.expand to take in array of tuples of input and output. It creates a new function for each 
tuple to check the input and output. For example: there are two tuples in array. So, @parameterized.expand
creates test_Placement_field_0 and test_Placement_field_1 as the function to perform tests."""
class PlacementsTestFailure(TestCase):
    @parameterized.expand([
        (2, 1),
        (1, 5)
    ])
    # This function tests the PowerRank field of Placement_1 table. It creates an object of table with the
    # given input PowerRank
    # and then uses self.assertEqual to check if
    @unittest.expectedFailure
    def test_Placement_field(self, input, expected):
        rank = Placements_1(Placement=input)
        self.assertEqual(rank.getPlacement(), expected)


    '''This function tests that the maximum length for the CharField representing a player's losses in an event is 100. A loop is traversed
        more than 100 times and each time a character is appended to a string that will eventually be greater than length 100. This
        string is then used to reporesent the player's losses for the newly created placement object. Because the CharField in the Placements_1 table
        has a max length of 100, it should not allow the player object to be created. As expected this test raises an error'''
    @unittest.expectedFailure
    def test_Losses_length(self):
        loss = ""
        for i in range(103):
            loss+=i
        place = Placements_1.objects.create(Year=2021, Region="North America", SmashggName="player", PowerRank=4, EventName="Autumn Championship", Placement="18", Losses=loss)
