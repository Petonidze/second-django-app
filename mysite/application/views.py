# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import user, notes
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    user_display = user.objects.all()
    notes_display = notes.objects.all().order_by("-date")[:20]
    return render(request, 'application/homePage.html', {"users":user_display, "notes":notes_display})

