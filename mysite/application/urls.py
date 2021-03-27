from django.urls import re_path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import user, notes

urlpatterns= [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=notes, template_name ="application/note.html"))
    
]