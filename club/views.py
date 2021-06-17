from django.shortcuts import get_object_or_404, render
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

@login_required
def new_meeting(request):
    form=MeetingForm
    if request.method == 'POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/new_meeting.html', {'form': form})

@login_required
def new_resource(request):
    form=ResourceForm
    if request.method == 'POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/new_resource.html', {'form': form})

def login_message(request):
    return render(request, 'club/login_message.html')

def logout_message(request):
    return render(request, 'club/logout_message.html')



