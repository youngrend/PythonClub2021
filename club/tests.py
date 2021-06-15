from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
# Create your tests here.

class Meeting_Test(TestCase):
    def setUp(self):
        self.meeting=Meeting(meeting_title='Meeting_1')
        
    def test_meetingstring(self):
        self.assertEqual(str(self.meeting), 'Meeting_1')

    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meetings')

class Meeting_Minutes_Test(TestCase):
    def setUp(self):
        self.meet_mins=Meeting_Minutes(minutes_text= 'SlammaJamma')
    
    def test_mins_string(self):
        self.assertEqual(str(self.meet_mins), 'SlammaJamma')

    def test_mins_table(self):
        self.assertEqual(str(Meeting_Minutes._meta.db_table), 'meeting_minutes')

class Resource_Test(TestCase):
    def setUp(self):
        self.resource=Resource(resource_name='PythonTest')

    def test_r_string(self):
        self.assertEqual(str(self.resource), 'PythonTest')

    def test_r_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class Event_Test(TestCase):
    def setUp(self):
        self.test=Event(event_title='PythonEvent')

    def test_event_string(self):
        self.assertEqual(str(self.test), 'PythonEvent')

    def test_event_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
        