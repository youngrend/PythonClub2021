from django.shortcuts import get_object_or_404, render
from .models import Meeting, Meeting_Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

def meeting_detail(request, id):
    meeting_detail=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meeting_detail.html', {'meeting_detail' : meeting_detail})