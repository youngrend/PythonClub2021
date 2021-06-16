from club.forms import MeetingForm
from django.test import TestCase
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm, ResourceForm
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

class MeetingForm_test(TestCase):
    def test_meetingform_is_valid(self):
        data={
            'meeting_title': 'meet1', 
            'meeting_date': '06/07/2021', 
            'meeting_time': '6:30',
            'meeting_location': 'meet_location',
            'meeting_agenda':'meet_agenda' 
            
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

    def test_meetingform_is_invalid(self):
        data={
            'meeting_title': 'meet1', 
            'meeting_date': '06/07/2021', 
            'meeting_time': '12 noon',
            'meeting_location': 'meet_location',
            'meeting_agenda':'meet_agenda' 
            
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)



        