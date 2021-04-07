from django.urls import re_path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import application_user, notes
from .views import UserCreate, UserUpdate, UserDelete, NoteCreate, NoteUpdate, NoteDelete, RegisterUser

urlpatterns= [

    re_path(r'^$', views.index, name = 'index'),

    re_path(r'^update-user/(?P<pk>\d+)$', UserUpdate.as_view(), name = 'update_user'),
    re_path(r'^delete-user/(?P<pk>\d+)$', UserDelete.as_view(), name = 'delete_user'),

    re_path(r'^add-note/$', NoteCreate.as_view(), name = 'add_note'),
    re_path(r'^update-note/(?P<pk>\d+)$', NoteUpdate.as_view(), name = 'update_note'),
    re_path(r'^delete-note/(?P<pk>\d+)$', NoteDelete.as_view(), name = 'delete_note'),

    #listing a special page for the unique note
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=notes, template_name ="application/note.html")),

    #register
    re_path(r'^register/$', RegisterUser.as_view(), name = 'register')
    
]