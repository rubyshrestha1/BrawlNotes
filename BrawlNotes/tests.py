import unittest
import datetime
from django.test import TestCase
from .models import Player_Registry, Official_1_Events, Placements_1
from parameterized import parameterized, parameterized_class
from django.urls import reverse,resolve
from django.test import Client
from .views import IndexViewEvents, placementDetails, IndexViewPlayers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

"""This class tests the views of the system"""
class TestView(TestCase):
    """This function tests view IndexViewEvents.It creates the Client object and is used to test whether the status
    code returned is 200. status code is 200 means that request has succeeded."""
    def test_index_events_status_code(self):
        client = Client()
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-events'))
        self.assertEquals(response.status_code, 200)

    """This function tests view IndexViewEvents.It creates the Client object and is used to test whether the template
    used is input templates"""
    def test_index_events_template_used(self):
        client = Client()
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-events'))
        self.assertTemplateUsed(response, 'BrawlNotes/indexEvent.html')

    """This function tests adding new users. It instantiates get_user_model() that returns currently active user
     model. Then custom object of that model is created. Finally object's email is tested against given email. """
    def test_add_users(self):
        user = get_user_model()
        user1 = user.objects.create_user(email ="test@tester.com", password="qwerty12345", date_of_birth = datetime.date(2000,1,1))
        self.assertEquals(user1.email, 'test@tester.com')

    """This function tests view IndexViewPlayers.It creates the Client object and is used to test whether the status
    code returned is 302. status code is 302 means that resource has been temporarily moved to another URL.
    This status code is used as user is first required to log in to view the list of players."""
    def test_index_players_status_code302(self):
        client = Client()
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertEquals(response.status_code, 302)

    """This function tests view IndexViewPlayers.It creates the Client object, instantiates get_user_model()
    that returns currently active user model. Then custom object of that model is created. The created user is
    logged into the system. Finally, status code of response is tested to check whether it is 200 (success)"""
    def test_index_players_status_code200(self):
        client = Client()
        user = get_user_model()
        user1 = user.objects.create_user(email ="test@tester.com", password="test12345", date_of_birth = datetime.date(2000,1,1))
        login = client.login(email="test@tester.com", password="test12345")
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertEqual(response.status_code, 200)

    """This function tests view IndexViewPlayers.It creates the Client object, instantiates get_user_model()
    that returns currently active user model. Then custom object of that model is created. The created user is
    logged into the system. Finally, the template used is tested against input templates"""
    def test_index_players_template_used_pass(self):
        client = Client()
        user = get_user_model()
        user1 = user.objects.create_user(email ="test@tester.com", password="test12345", date_of_birth = datetime.date(2000,1,1))
        login = client.login(email="test@tester.com", password="test12345")
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertTemplateUsed(response, 'BrawlNotes/indexPlayer.html')

    """This function tests view IndexViewPlayers.It creates the Client object, instantiates get_user_model()
    that returns currently active user model. Then custom object of that model is created. The created user is
    logged into the system. Finally, the template used is tested against input templates. This test is expected to fail
    as incorrect template is provided as input"""
    @unittest.expectedFailure
    def test_index_players_template_used_fail(self):
        client = Client()
        user = get_user_model()
        user1 = user.objects.create_user(email ="test@tester.com", password="test12345", date_of_birth = datetime.date(2000,1,1))
        login = client.login(email="test@tester.com", password="test12345")
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertTemplateUsed(response, 'BrawlNotes/indexPlayers.html')

    """This function tests view placementDetails.It creates the Client object and is used to test whether the status
    code returned is 200, which should be failed test as user is required to first log in to be able to view the page.
    response returns status code 302 which implies that resource has been temporarily moved to another URL (URL for user
    to log in)."""
    @unittest.expectedFailure
    def test_search_placement_status_code200_fail(self):
        client = Client()
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertEquals(response.status_code, 200)

    """This function tests placementDetails.It creates the Client object and is used to test whether the status
    code returned is 302. status code is 302 means that resource has been temporarily moved to another URL.
    This status code is used as user is first required to log in to view the list of players."""
    def test_search_placement_status_code302(self):
        client = Client()
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertEquals(response.status_code, 302)

    """This function tests placementDetails.It creates the Client object, instantiates get_user_model()
    that returns currently active user model. Then custom object of that model is created. The created user is
    logged into the system. Finally, status code of response is tested to check whether it is 200 (success) """
    def test_search_placements_status_code200_pass(self):
        client = Client()
        user = get_user_model()
        user1 = user.objects.create_user(email ="test@tester.com", password="test12345", date_of_birth = datetime.date(2000,1,1))
        login = client.login(email="test@tester.com", password="test12345")
        response = client.get(reverse('BrawlNotes:BrawlNotes-index-players'))
        self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response, 'BrawlNotes/indexPlayer.html')


""" This class is for testing the urls of different views. url of views are retrieved through reverse function which
is then compared with given input views to check whether they are same or not. """
class TestUrls(TestCase):
    """This function tests the url of view IndexViewEvents """
    def test_url_indexEvent(self):
        url = reverse('BrawlNotes:BrawlNotes-index-events')
        self.assertEquals( resolve(url).func.view_class, IndexViewEvents)

    """This function tests the url of view IndexViewEvents and is expected to fail as incorrect input view is provided """
    @unittest.expectedFailure
    def test_url_indexEvent_Fail(self):
        url = reverse('BrawlNotes:BrawlNotes-index-events')
        self.assertEquals( resolve(url).func.view_class, IndexViewEvent)

    """This function tests the url of view IndexViewPlayers """
    def test_url_indexPlayer(self):
        url = reverse('BrawlNotes:BrawlNotes-index-players')
        self.assertEquals( resolve(url).func.view_class, IndexViewPlayers)

    """This function tests the url of view placementDetails """
    def test_url_searchPlacement(self):
        url = reverse('BrawlNotes:BrawlNotes-search-placement')
        self.assertEquals( resolve(url).func, placementDetails)


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



