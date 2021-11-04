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

    """This function tests the region field of the PlayerRegistry table. A new player object is created 
       with NorthAmeri, 123 and Moon as Region, BrawlhallaID and SmashggName respectively. The function then asserts if
       the object's 'Region' field matches with the given value, which in case should fail. If they do not match, 
       message that says 'Region is not same' is displayed."""
    def test2_region_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=123, SmashggName="Moon")
        self.assertEqual("North Ameri", player1.Region, msg="Region is not same")  # fail

    """This function tests the region field of the PlayerRegistry table. A new player objects is created with 
        NorthAmerica, "200" and test  as Region, BrawlhallaID and SmashggName respectively.
         The function then asserts if the object's 'BrawlHallaID' field matches with the given ID value. The test fails
          in this case as type of BrawlHallaIDs are not consistent """
    def test_type_BrawlhallaID_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        self.assertEqual("200", player1.BrawlhallaID)  # Fail

    """This function tests the region field of the PlayerRegistry table. A new player objects is created with 
        NorthAmerica, 111 and test  as Region, BrawlhallaID and SmashggName respectively.
         The function then asserts if the object's 'BrawlHallaID' field matches with the given ID value. """
    def test_BrawlhallaID_field(self):
            player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
            self.assertEqual(111, player1.BrawlhallaID)  # Pass

    """This function tests the SmashggName field of the PlayerRegistry table. Two new player objects are created with 
           different region, BrawlHallaID and SmashggName. This function asserts if the 
           'SmashggName' field of same object matches. """
    def test_SmashggName_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        player2 = Player_Registry.objects.create(Region="South America", BrawlhallaID=101, SmashggName="test1")
        self.assertIs(player1, player2)


    """This function tests the SmashggName field of the PlayerRegistry table. Two new player objects are created with 
        different region and BrawlHalla ID but same SmashggName. Since SmashggName is primary key, it should not allow 
        creation of two objects with same SmashggName. As expected, this test raises integrity error."""
    def test_integrityError_SmashggName_field(self):
        player1 = Player_Registry.objects.create(Region="North America", BrawlhallaID=111, SmashggName="test")
        player2 = Player_Registry.objects.create(Region="South America", BrawlhallaID=100, SmashggName="test")



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

    # This functions tries to get the object created from setUpTestData using get method.
    # However, the function gives "object does not exist error" because with get method it is trying to
    # access something that has not been created at all.
    def test_objectError_eventName_field(self):
        event2 = Official_1_Events.objects.get(EventName="November Championship")


    # This functions gets the object created from setUpTestData and checks if year matches the given year.
    def test_Year_field(self):
        event1 = Official_1_Events.objects.get(Year=2021)
        self.assertEqual(2021, event1.Year)


"""
This class performs the parameterized test for one of the attributes of Placement_1 table in database. 
It uses @parameter.expand to take in array of tuples of input and output. It creates a new function for each 
tuple to check the input and output. For example: there are two tuples in array. So, @parameterized.expand
creates test_PowerRank_field_0 and test_PowerRank_field_1 as the function to perform tests."""
class PlacementsTest(TestCase):
    @parameterized.expand([
        (1, 1),
        (5, 1)  # This should fail.
    ])
    # This function tests the PowerRank field of Placement_1 table. It creates an object of table with the
    # given input PowerRank
    # and then uses self.assertEqual to check if
    def test_PowerRank_field(self, input, expected):
        rank = Placements_1(PowerRank=input)
        self.assertEqual(rank.getPowerRank(), expected)
