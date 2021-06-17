from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/',views.resources, name='resources'),
   path('meetings/',views.meetings, name='meetings'),
   path('meeting_detail/<int:id>',views.meeting_detail, name='meeting_detail'),
   path('new_meeting/', views.new_meeting, name='new_meeting'),
   path('new_resource/', views.new_resource, name='new_resource'),
   path('login_message/', views.login_message, name='login_message'),
   path('logout_message/', views.logout_message, name='logout_message')
]