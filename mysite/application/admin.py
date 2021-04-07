# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import application_user, notes

admin.site.register(application_user)
admin.site.register(notes)
# Register your models here.
