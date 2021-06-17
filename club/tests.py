from club.forms import MeetingForm
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.urls import reverse, reverse_lazy
import datetime
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
        self.test_user=User.objects.create_user(username='user1')
        self.resource=Resource(
            resource_name='PythonTest',
            resource_type='Educational',
            resource_url='http://www.python.org',
            resource_date_entered= '06/07/2021',
            resource_description= 'description'
            )
        
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

class New_Resource_Auth_Test(TestCase): 
    def setUp(self):
        self.test_user=User.objects.create_user(user_id='user1', password='DYdy6839!')
        self.test_resource=Resource.objects.create(
            resource_name='PythonTest',
            resource_type='Educational',
            resource_url='http://www.python.org',
            resource_date_entered= '06/07/2021',
            resource_description= 'description'
        )
    def redirect_if_not_logged_in(self):
        response=self.client.get(reverse('new_resource'))
        self.assertRedirects(response, '/accounts/login?next=/club/new_meeting/')            




        