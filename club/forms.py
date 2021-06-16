from django import forms
from .models import Meeting, Meeting_Minutes, Resource, Event   

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'